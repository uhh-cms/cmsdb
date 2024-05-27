# coding: utf-8

__all__ = []

# adjust the path to import cmsdb
import os
import sys
base = os.path.normpath(os.path.join(os.path.abspath(__file__), "../.."))
sys.path.append(base)

# import all tests
from .test_processes import *  # noqa
from .test_campaigns import *  # noqa
