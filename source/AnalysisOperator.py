import os
import sys
import pandas as pd
import RegexHelper
class AnalysisOperator():
    """ 
    Class, which produces and analyses the lines of text
    """
    def __init__(self, config, log = True):
        """ Constructor method """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "AnalysisOperator"
        #: Configuration dictionary
        self.Config = dict(config[self.OperatorName])
        #: Column name
        self.ColName = 'Counts'
        #: A dataframe to analyse 
        self.Dataframe = pd.DataFrame(columns=[self.ColName])
        self.Introduce()

    def ProduceDataframe(self, generator):
        """ Produces a dataframe object from the generator """
        general_dict = {}
        for line in generator:
            words = RegexHelper.GetWords(line)
            for word in words:
                if word in general_dict.keys():
                    general_dict[word] += 1
                else:
                    general_dict[word] = 1
        self.Dataframe = pd.DataFrame.from_dict(general_dict, 
                orient='index', columns = [self.ColName])
        self.Dataframe = self.Dataframe.sort_values(by=[self.ColName], 
                ascending = False)

    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)
    def Introduce(self):
        """ Method to introduce """
        self.Log("%s loaded. It will analyse your lines."%self.OperatorName)
