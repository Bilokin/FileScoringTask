#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
import RegexHelper
class AnalysisOperator():
    """ 
    Class, which produces and analyses the lines of text
    """
    def __init__(self, config, log = True):
        """ 
        Constructor method 
        Args:
            config (dict): Configuration dictionary, 
                it has to contain a key named after
                this operator
            log (bool): switch to disable logs
        Returns: 
        """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "AnalysisOperator"
        #: Configuration dictionary
        self.Config = dict(config[self.OperatorName])
        #: Column name
        self.ColName = 'Counts'
        #: Dict filename: DataFrame
        self.DataframeDict = {}
        self.Introduce()

    def ProduceDataframe(self, generator):
        """ 
        Produces a dataframe object from the generator 
        Args:
            generator (obj): Iterative object of strings
        Returns:
            df (pandas.DataFrame): Sorted DataFrame of counts
        """
        general_dict = {}
        for line in generator:
            words = RegexHelper.GetWords(line)
            for word in words:
                if word in general_dict:
                    general_dict[word] += 1
                else:
                    general_dict[word] = 1
        df = pd.DataFrame.from_dict(general_dict, 
                orient='index', columns = [self.ColName])
        df = df.sort_values(by=[self.ColName], 
                ascending = False)
        return df

    def AnalyseFile(self, generator, fileName):
        """ 
        Produces a dataframe and integrates it into a common dict 
        Args:
            generator (obj): Iterative object of strings
            fileName (str): Name of the analysed file
        Returns: None
        """
        self.DataframeDict[fileName] = self.ProduceDataframe(generator)

    def GetMergedData(self):
        """ 
        Returns a merged dataframe sorted by counts 
        Args:
        Returns:
            df (pandas.DataFrame): Sorted DataFrame of counts
        """
        df = pd.DataFrame(columns = [self.ColName])
        for value in self.DataframeDict.values():
            df = df.add(value, fill_value = 0)
        df = df.sort_values(by=[self.ColName],
            ascending = False)
        return df

    def Log(self, string):
        """ 
        Log method, prints a preformatted message. 
        Args:
            string (str): String to print
        """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce """
        self.Log("%s loaded. It will analyse your lines."%self.OperatorName)
