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
        lines = ['intellegis quanta in dato beneficio sit laus, cum in accepto sit tanta gloria.',
                'Intellectum est enim mihi quidem in multis, et maxime in me ipso, sed paulo ']
        #analysisOperator.ProduceDataframe(lines)
        print(analysisOperator.Dataframe.head)

if __name__ == '__main__':
    unittest.main()
