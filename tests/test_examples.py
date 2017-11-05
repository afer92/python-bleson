#!/usr/bin/env python3

# A test to run all the example scripts to check for basic compilation or unexpected runtime exceptions
# Does not validate the correctness of any example
# All examples should return in a timely manor. TODO: add a forced timeout to this script executor.

import sys
import os
import glob

import unittest
import runpy

from bleson.logger import log

TEST_DURATION=1

class TestExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        examples_path = os.path.join(dir_path, '..', 'examples')
        examples_glob = os.path.join(examples_path, '*.py')

        cls.scripts = glob.glob(examples_glob)
        log.debug(cls.scripts)

    def test_all_examples(self):
        for script in self.scripts:
            log.info("Running {}".format(script))
            sys.argv = ['', str(TEST_DURATION)]
            runpy.run_path(script)

