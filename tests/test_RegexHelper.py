#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../source'))
import RegexHelper

class TestRegexHelper(unittest.TestCase):
    """Test case for regex helper """

    def test_GetWords(self):
        """ Test GetWords method """
        phrase = 'Adolescebat autem obstinatum propositum erga haec et similia multa scrutanda,'
        words = RegexHelper.GetWords(phrase)
        print(words)
        self.assertEqual(len(words),10)
        self.assertEqual(words[-1],'scrutanda')
        
        phrase = ' p_beam      = (0.175903,0,4.49595;11.4946)'
        words = RegexHelper.GetWords(phrase)
        print(words)
        self.assertEqual(len(words),1)


if __name__ == '__main__':
    unittest.main()
