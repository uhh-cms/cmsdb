# test_module.py
import os
import unittest
import sys
from glob import glob
import importlib as imp


class TestCampaign(unittest.TestCase):
    @unittest.skipIf("TESTMODULE" not in os.environ, "TESTMODULE not set")
    @unittest.skipIf(
        os.environ["TESTMODULE"].strip("/").endswith("run2_2016_nano_v9"),
        "Tests for module 'run2_2016_nano_v9' are not implemented yet.",
    )
    @unittest.skipIf(
        os.environ["TESTMODULE"].strip("/").endswith("__pycache__"),
        "'__pycache__' is not a valid module.",
    )
    @classmethod
    def setUpClass(cls):
        modpath = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
        if modpath not in sys.path:
            sys.path.append(modpath)
        mod = os.environ["TESTMODULE"]
        to_import = os.path.relpath(mod, modpath).replace("/", ".")
        # Load the module to test
        cls.module = imp.import_module(to_import)

        # get all submodules
        all_objects = getattr(cls.module, "__all__", None)
        cls.submodules = list()
        if not isinstance(all_objects, list):
            basename = cls.module.__name__.split(".")[-1]
            object_name = f"campaign_{basename}"
            cls.submodules = {object_name: getattr(cls.module, object_name)}
        else:
            cls.submodules = {x: getattr(cls.module, x) for x in all_objects}

    def test_campaign_properties(self):
        # loop through the different campaign objects in the current module
        for name, submodule in self.submodules.items():
            # run the test for each submodule
            with self.subTest(f"testing object {name}"):
                # make sure the campaign defines a basic set of properties
                self.assertTrue(hasattr(submodule, "name"))
                self.assertTrue(hasattr(submodule, "id"))
                self.assertTrue(hasattr(submodule, "ecm"))
                self.assertTrue(hasattr(submodule, "bx"))

    def test_campaign_datasets(self):
        # loop through the different campaign objects in the current module
        for campaign_name, submodule in self.submodules.items():
            # run the test for each submodule
            with self.subTest(f"testing dataset of object '{campaign_name}'"):
                # make sure the campaign defines datasets in the first place
                self.assertTrue(hasattr(submodule, "datasets"))
                datasets = submodule.datasets
                # loop through the datasets and test their properties
                for dataset_name, _, dataset in datasets.items():
                    with self.subTest(f"testing dataset {campaign_name}/{dataset_name}"):
                        # might want to implement naming conventions here,
                        # e.g. the name of the dataset is the process name + suffix
                        self.assertTrue(hasattr(dataset, "name"))
                        self.assertTrue(hasattr(dataset, "id"))
                        self.assertTrue(hasattr(dataset, "processes"))
                        self.assertTrue(hasattr(dataset, "keys"))
                        self.assertTrue(hasattr(dataset, "n_files"))
                        self.assertTrue(hasattr(dataset, "n_events"))


if __name__ == "__main__":
    # Remove command line arguments before running unittest.main()
    # to prevent unittest from trying to interpret them
    # if cmsdb is not path of the sys path, add it
    unittest.main()
