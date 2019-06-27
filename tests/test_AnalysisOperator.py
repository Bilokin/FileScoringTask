#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../source'))
from AnalysisOperator import AnalysisOperator
from FileReader import FileReader

class TestAnalysisOperator(unittest.TestCase):
    """Test case for analysis operator """

    def test_ProduceDataframe(self):
        """ Test produce dataframe method """
        fileNames = ['tests/examples/lorem.txt',
                'tests/examples/lorem-eng.txt']
        analysisOperator = AnalysisOperator({"AnalysisOperator":{}})
        with FileReader(fileNames) as fileReader:
            analysisOperator.ProduceDataframe(fileReader.Read())
        self.assertEqual(analysisOperator.Dataframe.loc['et']['Counts'],37)
        self.assertEqual(analysisOperator.Dataframe.loc['in']['Counts'],26)
        self.assertEqual(analysisOperator.Dataframe.loc['ut']['Counts'],13)
        self.assertEqual(analysisOperator.Dataframe.loc['the']['Counts'],12)
        self.assertEqual(analysisOperator.Dataframe.loc['est']['Counts'],10)
        self.assertEqual(analysisOperator.Dataframe.loc['ad']['Counts'],10)
        self.assertEqual(analysisOperator.Dataframe.loc['enim']['Counts'],9)
        

if __name__ == '__main__':
    unittest.main()
