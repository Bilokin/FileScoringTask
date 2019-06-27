import matplotlib.pyplot as plt

class PlotOperator():
    """ 
    Class, which plots the plots
    """
    def __init__(self, config, log = True):
        """ Constructor method """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "PlotOperator"
        #: Configuration dictionary
        self.Config = dict(config[self.OperatorName])
        self.Introduce()

    def Plot(self, dataframe):
        """ Plots a dataframe """
        if (len(dataframe) < 1):
            # TODO: print a meaningful message
            return
        dataframe.plot.barh()
        plt.tight_layout()
        plt.show()

    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce itself """
        self.Log("%s loaded. It will plot your plots."%self.OperatorName)
