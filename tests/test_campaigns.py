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

    def test_campaign_aux(self):
        for campaign_inst in self.campaigns.values():
            with self.subTest(f"testing {campaign_inst.name}"):
                # field existence
                self.assertTrue(campaign_inst.has_aux("tier"))
                self.assertTrue(campaign_inst.has_aux("run"))
                self.assertTrue(campaign_inst.has_aux("year"))
                self.assertTrue(campaign_inst.has_aux("version"))
                self.assertTrue(campaign_inst.has_aux("postfix"))
                # field types
                self.assertIsInstance(campaign_inst.x.tier, str)
                self.assertIsInstance(campaign_inst.x.run, int)
                self.assertIsInstance(campaign_inst.x.year, int)
                self.assertIsInstance(campaign_inst.x.version, int)
                self.assertIsInstance(campaign_inst.x.postfix, str)

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
            for dataset_info_key, dataset_info in dataset_inst.info.items():

                dataset_string = (
                    f"{campaign_inst.name}/{dataset_inst.name}/{dataset_info_key}, keys: {dataset_info.keys}"
                )
                das_infos = [get_das_info(key) for key in dataset_info.keys]
                for das_info in das_infos:
                    with self.subTest(f"checking existence of DAS key {das_info['name']} from {dataset_string}"):
                        self.assertTrue(das_info.get("dataset_id", None) is not None)

                with self.subTest(f"checking DAS infos from {dataset_string}"):
                    combined_das_info = {
                        "dataset_id": das_infos[0]["dataset_id"],
                        "nevents": sum(info["nevents"] for info in das_infos),
                        "nfiles": sum(info["nfiles"] for info in das_infos),
                    }
                    combined_dataset_info = {
                        "dataset_id": dataset_inst.id,
                        "nevents": dataset_info.n_events,
                        "nfiles": dataset_info.n_files,
                    }
                    if dataset_info_key != "nominal":
                        # compare IDs only when checking the nominal dataset
                        combined_das_info.pop("dataset_id")
                        combined_dataset_info.pop("dataset_id")

                    self.assertEqual(
                        combined_dataset_info,
                        combined_das_info,
                        msg=f"mismatch in DAS info from {dataset_string}",
                    )

    def test_campaign_datasets(self):
        for campaign_inst in self.campaigns.values():
            with self.subTest(f"testing datasets {campaign_inst.name}"):
                # make sure the campaign defines datasets in the first place
                self.assertTrue(hasattr(campaign_inst, "datasets"))

                # loop through the datasets and test their properties
                for dataset_inst in campaign_inst.datasets.values():
                    with self.subTest(f"testing dataset {campaign_inst.name}/{dataset_inst.name}"):
                        self.single_dataset_test(campaign_inst, dataset_inst)
