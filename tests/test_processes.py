# coding: utf-8

from __future__ import annotations

__all__ = ["TestProcesses"]

import unittest
import collections

import order as od

import cmsdb


class TestProcesses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # find processes and store them
        cls.processes = {
            name: process_inst
            for name in dir(cmsdb.processes)
            if isinstance((process_inst := getattr(cmsdb.processes, name)), od.Process)
        }

    def test_process_properties(self):
        for process_name, process_inst in self.processes.items():
            with self.subTest(f"testing {process_inst.name}"):
                self.assertTrue(hasattr(process_inst, "name"))
                self.assertTrue(hasattr(process_inst, "id"))

                # process name should be equivalent to the process instance's name
                self.assertEqual(process_name, process_inst.name)

                # check that the name is lowercase, but take into account known exceptions
                if not process_inst.x("allow_uppercase_name", False):
                    self.assertEqual(process_inst.name, process_inst.name.lower())

    def test_unique_names_and_ids(self):
        name_counts = collections.Counter(
            process_inst.name
            for process_inst in self.processes.values()
        )
        dup_names = {name: count for name, count in name_counts.items() if count > 1}
        if dup_names:
            self.fail(f"duplicate process names found: {dup_names}")

        id_counts = collections.Counter(
            process_inst.id
            for process_inst in self.processes.values()
        )
        dup_ids = {id_: count for id_, count in id_counts.items() if count > 1}
        if dup_ids:
            self.fail(f"duplicate process ids found: {dup_ids}")
