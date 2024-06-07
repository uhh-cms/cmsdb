# coding: utf-8

__all__ = ["TestCampaigns"]

import os
import re
import importlib
import unittest

import cmsdb


class TestCampaigns(unittest.TestCase):
    generator_names = ("powheg", "madgraph", "amcatnlo", "pythia")

    check_proc_name: bool = False

    @classmethod
    def setUpClass(cls):
        # find campaigns
        campaign_dir = os.path.join(os.path.dirname(cmsdb.__file__), "campaigns")
        campaign_names = [
            name
            for name in os.listdir(campaign_dir)
            if os.path.isdir(os.path.join(campaign_dir, name)) and re.match(r"^run\d.*v\d.*$", name)
        ]

        # import modules and store campaign objects if present
        cls.campaigns = {}
        for name in campaign_names:
            module = importlib.import_module(f"cmsdb.campaigns.{name}")
            for attr in dir(module):
                if attr.startswith("campaign_"):
                    cls.campaigns[name] = getattr(module, attr)

    def test_campaign_properties(self):
        for campaign_inst in self.campaigns.values():
            with self.subTest(f"testing {campaign_inst.name}"):
                self.assertTrue(hasattr(campaign_inst, "name"))
                self.assertTrue(hasattr(campaign_inst, "id"))
                self.assertTrue(hasattr(campaign_inst, "ecm"))
                self.assertTrue(hasattr(campaign_inst, "bx"))

    def test_campaign_datasets(self):
        for campaign_inst in self.campaigns.values():
            with self.subTest(f"testing datasets {campaign_inst.name}"):
                # make sure the campaign defines datasets in the first place
                self.assertTrue(hasattr(campaign_inst, "datasets"))

                # loop through the datasets and test their properties
                for dataset_inst in campaign_inst.datasets.values():
                    with self.subTest(f"testing dataset {campaign_inst.name}/{dataset_inst.name}"):
                        # check existence of attributes
                        self.assertTrue(hasattr(dataset_inst, "name"))
                        self.assertTrue(hasattr(dataset_inst, "id"))
                        self.assertTrue(hasattr(dataset_inst, "processes"))
                        self.assertTrue(hasattr(dataset_inst, "keys"))
                        self.assertTrue(hasattr(dataset_inst, "n_files"))
                        self.assertTrue(hasattr(dataset_inst, "n_events"))

                        # check that the generator is encoded in the dataset name
                        if "data" not in dataset_inst.name:
                            self.assertTrue(any(f"_{name}" in dataset_inst.name for name in self.generator_names))

                        # check that the name is lowercase, but take into account known exceptions
                        if not dataset_inst.x("allow_uppercase_name", False):
                            self.assertEquals(dataset_inst.name, dataset_inst.name.lower())

                        # check that there is at least one process linked
                        self.assertTrue(len(dataset_inst.processes) > 0)

                        # optionally check that namings between dataset and process are consistent
                        if (
                            self.check_proc_name and
                            "data" not in dataset_inst.name and
                            len(dataset_inst.processes) == 1
                        ):
                            proc_name = dataset_inst.processes.get_first().name

                            if "data" not in dataset_inst.name:
                                dataset_name_wo_generator = dataset_inst.name
                                for name in self.generator_names:
                                    dataset_name_wo_generator = dataset_name_wo_generator.replace(f"_{name}", "")

                                self.assertEqual(dataset_name_wo_generator, proc_name)
