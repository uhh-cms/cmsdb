# test_module.py
import os
import unittest
import sys
from glob import glob
import importlib as imp


class TestCampaign(unittest.TestCase):
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
        for name, submodule in self.submodules.items():
            with self.subTest(f"testing object {name}"):
                self.assertTrue(hasattr(submodule, "name"))
                self.assertTrue(hasattr(submodule, "id"))
                self.assertTrue(hasattr(submodule, "ecm"))
                self.assertTrue(hasattr(submodule, "bx"))


if __name__ == "__main__":
    # Remove command line arguments before running unittest.main()
    # to prevent unittest from trying to interpret them
    # if cmsdb is not path of the sys path, add it
    unittest.main()
