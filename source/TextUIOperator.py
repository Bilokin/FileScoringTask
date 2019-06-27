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

    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce itself """
        self.Log("%s loaded. It will interact with user via console."%self.OperatorName)
