import os
import sys
class FileReader():
    """ This class simply reads a file in a lazy way """
    def __init__(self, fileName, log = True):
        """ Constructor method """
        self.enableLogging = log
        self.OperatorName = "FileReader"
        self.Status = 'Invalid'
        self.File = None
        self.FileName = fileName
    def __enter__(self):
        if os.path.isfile(self.FileName):
            self.Log('Opening a file %s'%self.FileName)
            self.File = open(self.FileName)
        else:
            # TODO: throw a meaningful exception
            self.Log('ERROR: file %s does not exists'%self.FileName)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.unlink(self.FileName)
    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)
    def Introduce(self):
        self.Log("%s loaded. It will open the file and read it by lines."%self.OperatorName)
