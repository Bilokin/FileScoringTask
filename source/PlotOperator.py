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

    def Plot(self, df):
        """ Plots a dataframe """
        if (len(df) < 1):
            # TODO: print a meaningful message
            return
        if isinstance(df, dict):
            for key in df.keys():
                if (len(df[key]) < 1):
                    continue
                # TODO: Make a pretty single plot
                ax = df[key].head(self.Config['NEntries']).plot.barh()
                ax.set_title(key)
                plt.tight_layout()
        else:
            df.head(self.Config['NEntries']).plot.barh()
            plt.tight_layout()
        plt.show()

    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)

    def Introduce(self):
        """ Method to introduce itself """
        self.Log("%s loaded. It will plot your plots."%self.OperatorName)
