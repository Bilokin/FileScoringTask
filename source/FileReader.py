import os
import sys
class FileReader():
    """ 
    Simple wrapper class that reads a file in a lazy way.
    It has to ensure that the words will not split up. 
    """
    def __init__(self, fileName, log = True):
        """ Constructor method """
        self.enableLogging = log
        self.OperatorName = "FileReader"
        self.Status = 'Invalid'
        self.File = None
        self.FileName = fileName

    def __enter__(self):
        """ Method to enter with statement, opens a file """
        if os.path.isfile(self.FileName):
            self.Log('Opening a file %s'%self.FileName)
            self.File = open(self.FileName)
        else:
            # TODO: throw a meaningful exception
            self.Log('ERROR: file %s does not exists'%self.FileName)
        return self

    def Read(self):
        """Lazy read method for big files, yields one line at a time"""
        for cnt, line in enumerate(self.File):
           yield line 
    def __exit__(self, exc_type, exc_value, traceback):
        """ Method to exit with statement """
        self.File.close()
    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)
    def Introduce(self):
        self.Log("%s loaded. It will open the file and read it by lines."%self.OperatorName)
