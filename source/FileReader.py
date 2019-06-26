import os
import sys
class FileReader():
    """ 
    Simple wrapper class that reads files in a lazy way.
    It has to ensure that the words will not split up. 
    """
    def __init__(self, fileNames, log = True):
        """ Constructor method """
        #: bool to enable logs
        self.enableLogging = log
        #: name of the class 
        self.OperatorName = "FileReader"
        #: List of file objects
        self.Files = []
        #: List of file names, strings
        self.FileNames = fileNames

    def __enter__(self):
        """ Method to enter with statement, opens files """
        for fileName in self.FileNames:
            if os.path.isfile(fileName):
                self.Log('Opening a file %s'%fileName)
                self.Files += [open(fileName)]
            else:
                # TODO: throw a meaningful exception
                self.Log('ERROR: file %s does not exists'%fileName)
        return self

    def Read(self):
        """Lazy read method for big files, yields one line at a time"""
        for txtFile in self.Files:
            for cnt, line in enumerate(txtFile):
               yield line 
    def __exit__(self, exc_type, exc_value, traceback):
        """ Method to exit with statement, close all opened files """
        for txtFile in self.Files:
            txtFile.close()
    def Log(self, string):
        """ Log method, prints a preformatted message. """
        if self.enableLogging:
            print(self.OperatorName+": "+string)
    def Introduce(self):
        """  """
        self.Log("%s loaded. It will open the file and read it by lines."%self.OperatorName)
