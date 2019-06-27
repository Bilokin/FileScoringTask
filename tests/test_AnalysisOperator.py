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
        df = None
        with FileReader(fileNames) as fileReader:
            df = analysisOperator.ProduceDataframe(fileReader.Read())
        self.assertEqual(df.loc['et']['Counts'],37)
        self.assertEqual(df.loc['in']['Counts'],26)
        self.assertEqual(df.loc['ut']['Counts'],13)
        self.assertEqual(df.loc['the']['Counts'],12)
        self.assertEqual(df.loc['est']['Counts'],10)
        self.assertEqual(df.loc['ad']['Counts'],10)
        self.assertEqual(df.loc['enim']['Counts'],9)

    def test_AnalyseFile(self) :
        fileNames = ['tests/examples/lorem.txt',
                    'tests/examples/lorem-eng.txt']
        analysisOperator = AnalysisOperator({"AnalysisOperator":{}})
        for fileName in fileNames:
            with FileReader(fileName) as fileReader:
                analysisOperator.AnalyseFile(fileReader.Read(), fileName)
        self.assertEqual(len(analysisOperator.DataframeDict),2)

    def test_GetMergedData(self) :
        fileNames = ['tests/examples/lorem.txt',
                    'tests/examples/lorem-eng.txt']
        analysisOperator = AnalysisOperator({"AnalysisOperator":{}})
        for fileName in fileNames:
            with FileReader(fileName) as fileReader:
                analysisOperator.AnalyseFile(fileReader.Read(), fileName)
        #print(analysisOperator.DataframeDict)
        df = analysisOperator.GetMergedData()
        self.assertEqual(df.loc['et']['Counts'],37)
        self.assertEqual(df.loc['in']['Counts'],26)
        self.assertEqual(df.loc['ut']['Counts'],13)
        self.assertEqual(df.loc['the']['Counts'],12)
        self.assertEqual(df.loc['est']['Counts'],10)
        self.assertEqual(df.loc['ad']['Counts'],10)
        self.assertEqual(df.loc['enim']['Counts'],9)

        


if __name__ == '__main__':
    unittest.main()
