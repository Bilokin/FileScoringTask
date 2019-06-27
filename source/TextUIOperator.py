#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TextUIOperator():
    """ 
    Class, which interacts with user
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
        self.OperatorName = "TextUIOperator"
        #: Configuration dictionary
        self.Config = dict(config[self.OperatorName])
        self.Introduce()

    def Say(self, message):
        """ 
        Prints a message to user 
        Args:
            message (str): Message to deliver
        """
        print(message)

    def PrintData(self, df):
        """ 
        Prints data in a desired format 
        Args:
            df (pandas.DataFrame): Data to print
        """
        self.Say('Printing out the most frequently used words:')
        if isinstance(df, dict):
            for key in df.keys():
                print('File: %s'%key)
                if (len(df[key]) < 1):
                    print('\tEmpty, not a text file or a directory.')
                else:
                    print(df[key].head(self.Config['NEntries']))
        else:
            print(df.head(self.Config['NEntries']))

    def Log(self, string):
        """ 
        Log method, prints a preformatted message. 
        Args:
            string (str): String to print
        """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce itself """
        self.Log("%s loaded. It will interact with user via console."%self.OperatorName)
