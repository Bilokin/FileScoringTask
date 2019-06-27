class TextUIOperator():
    """ 
    Class, which interacts with user
    """
    def __init__(self, config, log = True):
        """ Constructor method """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "TextUIOperator"
        #: Configuration dictionary
        self.Config = dict(config[self.OperatorName])
        self.Introduce()

    def Say(self, message):
        """ Prints a message to user """
        print(message)
    def PrintData(self, df):
        """ Prints data in a desired format """
        if isinstance(df, dict):
            for key in df.keys():
                print('File: %s'%key)
                print(df[key].head(self.Config['NEntries']))
        else:
            print(df.head(self.Config['NEntries']))
    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce itself """
        self.Log("%s loaded. It will interact with user via console."%self.OperatorName)
