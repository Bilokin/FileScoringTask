import os
import sys
import pandas as pd
import RegexHelper
class AnalysisOperator():
    """ 
    """
    def __init__(self, config, log = True):
        """ Constructor method """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "AnalysisOperator"
        #: Configuration dictionary
        self.Config = config[self.OperatorName]
        #: A dataframe to analyse 
        self.Dataframe = pd.DataFrame(columns=['Counts'])

    def ProduceDataframe(self, generator):
        """ Produces a dataframe object from the generator """
        for line in generator:
            wordDF = pd.DataFrame(index =
                    RegexHelper.GetWords(line)).index.value_counts().to_frame("Counts")
            self.Log(str(wordDF))
            for word, count in wordDF.iterrows():
                if word in self.Dataframe.index:
                    print(word)
                    self.Dataframe['Counts'][word] += count
                else:
                    self.Dataframe.loc[word] = [count]

    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)
    def Introduce(self):
        """ Method to introduce """
        self.Log("%s loaded. It will open the file and read it by lines."%self.OperatorName)
