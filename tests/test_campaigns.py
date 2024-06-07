# coding: utf-8

from __future__ import annotations

__all__ = ["TestCampaigns"]


import os
import re
import importlib
import unittest

import cmsdb

from scripts.get_das_info import get_das_info


class TestCampaigns(unittest.TestCase):
    # list of generator names to check for in dataset names
    generator_names = ("powheg", "madgraph", "amcatnlo", "pythia")

    # boolean flag whether to check consistency between dataset and process names
    check_proc_name: bool = False

    # boolean flag whether to check correctness of DAS info for each dataset
    check_das_info: bool = False

    # list of campaign names to test, if None, all campaigns are tested
    campaign_names: list | None = None

    @classmethod
    def setUpClass(cls):
        if not cls.campaign_names:
            # if not provided, find and test all campaigns
            campaign_dir = os.path.join(os.path.dirname(cmsdb.__file__), "campaigns")
            cls.campaign_names = [
                name
                for name in os.listdir(campaign_dir)
                if os.path.isdir(os.path.join(campaign_dir, name)) and re.match(r"^run\d.*v\d.*$", name)
            ]

        # import modules and store campaign objects if present
        cls.campaigns = {}
        for name in cls.campaign_names:
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

    def single_dataset_test(self, campaign_inst, dataset_inst):
        # check existence of attributes
        self.assertTrue(hasattr(dataset_inst, "name"))
        self.assertTrue(hasattr(dataset_inst, "id"))
        self.assertTrue(hasattr(dataset_inst, "processes"))
        self.assertTrue(hasattr(dataset_inst, "keys"))
        self.assertTrue(hasattr(dataset_inst, "n_files"))
        self.assertTrue(hasattr(dataset_inst, "n_events"))

        # check that the generator is encoded in the dataset name
        if dataset_inst.is_mc:
            self.assertIn(dataset_inst.name.rsplit("_", 1)[-1], self.generator_names)

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

        if self.check_das_info and not campaign_inst.has_aux("custom"):
            # check that all dataset keys exist and that the DAS info (id, n_events, n_files) is correct
            # optional, since this needs a Grid Proxy and takes a long time
            for key in dataset_inst.keys:
                key_info = f"{campaign_inst.name}/{dataset_inst.name}, key: {key}"
                # print(f"checking DAS info from dataset {campaign_inst.name}/{dataset_inst.name}, key {key}")
                das_info = get_das_info(key)
                with self.subTest(f"checking DAS info from {key_info}"):
                    das_info = get_das_info(key)
                    self.assertTrue(
                        das_info.get("dataset_id", None) is not None,
                        msg=f"did not find DAS key from {key_info}",
                    )

                    das_info = {
                        key: value for key, value in das_info.items()
                        if key in ("dataset_id", "nevents", "nfiles")
                    }

                    dataset_info = {
                        "dataset_id": dataset_inst.id,
                        "nevents": dataset_inst.n_events,
                        "nfiles": dataset_inst.n_files,
                    }
                    self.assertEqual(dataset_info, das_info, msg=f"mismatch in DAS info from {key_info}")

    def test_campaign_datasets(self):
        for campaign_inst in self.campaigns.values():
            with self.subTest(f"testing datasets {campaign_inst.name}"):
                # make sure the campaign defines datasets in the first place
                self.assertTrue(hasattr(campaign_inst, "datasets"))

                # loop through the datasets and test their properties
                for dataset_inst in campaign_inst.datasets.values():
                    with self.subTest(f"testing dataset {campaign_inst.name}/{dataset_inst.name}"):
                        self.single_dataset_test(campaign_inst, dataset_inst)
