#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../source'))
from FileReader import FileReader

class TestFileReader(unittest.TestCase):
    """Test case for file reader"""

    def test_Read(self):
        """ Checks the basic functionality """
        counter = 0
        # TODO: relative path is not optimal...
        fileNames = ['tests/examples/lorem.txt',
                'tests/examples/lorem-eng.txt']
        with FileReader(fileNames) as fileReader:
            for line in fileReader.Read():
                counter += 1
        self.assertEqual(counter, 105)
    def test_ReadLarge(self):
        """ Checks the performance """
        # TODO: do the actual check of performance
        counter = 0
        fileNames = 'tests/examples/RecoDecays.out'
        with FileReader(fileNames) as fileReader:
            for line in fileReader.Read():
                counter += 1
        self.assertEqual(counter, 413462)

if __name__ == '__main__':
    unittest.main()
