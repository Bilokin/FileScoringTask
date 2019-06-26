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
        with FileReader('tests/examples/lorem.txt') as fileReader:
            fileReader.Log('Here!')
if __name__ == '__main__':
    unittest.main()
