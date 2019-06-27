#!/usr/bin/env python3
import os
import sys
import argparse
import glob

sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))
from AnalysisOperator import AnalysisOperator
from FileReader import FileReader
from TextUIOperator import TextUIOperator
from PlotOperator import PlotOperator

def GetFileNames(args):
    """ Function, which selects the file names """
    if (args.filename):
        return [args.filename]
    if (args.directoryname):
        fileNames = glob.glob(args.directoryname+'/*')
        # TODO: filter away non-text files
        return fileNames
    cwd = os.getcwd()
    # TODO: filter away non-text files
    fileNames = glob.glob(cwd+'/*')
    return fileNames


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",  help="File to analyse", action="store")
    parser.add_argument("-d", "--directoryname",  help="Directory to analyse", action="store")
    parser.add_argument("-p", "--plot",  help="Plot the hist", action="store_true")
    args = parser.parse_args()
    # TODO: move config to a separate file
    config = {'AnalysisOperator':{}, 
              'TextUIOperator':{},
              'PlotOperator':{}}
    # Load main operators
    uiOperator = TextUIOperator(config)
    analysisOperator = AnalysisOperator(config)
    fileNames = GetFileNames(args)
    # Read files
    with FileReader(fileNames) as fileReader:
        analysisOperator.ProduceDataframe(fileReader.Read())
    uiOperator.Say('Printing out the 10 most frequent words:')
    uiOperator.Say(analysisOperator.Dataframe.head(10))
    # Make a plot on user request only
    if (args.plot):
        plotOperator = PlotOperator(config)
        plotOperator.Plot(analysisOperator.Dataframe.head(10))

