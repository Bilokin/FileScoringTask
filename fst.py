#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    """ 
    Function, which selects the file names 
    Args:
        args (obj): Arguments of argparse 
    Returns: 
        (bool) list of the filenames
    """
    if (args.filename):
        return [args.filename]
    if (args.directoryname):
        # TODO: This is not optimal
        fileNames = glob.glob(args.directoryname+'/*')
        # TODO: filter away non-text files
        return fileNames
    cwd = os.getcwd()
    # TODO: filter away non-text files
    fileNames = glob.glob(cwd+'/*')
    return fileNames


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to count the most frequent words '
        'in a file or directory. It is able to plot the histograms or print them to console.')
    parser.add_argument("-f", "--filename",  
            help="Path to file for the analysis", action="store")
    parser.add_argument("-d", "--directoryname",  
            help="Path to directory for the analysis", action="store")
    parser.add_argument("-p", "--plot",  
            help="Plot the histogram", action="store_true")
    parser.add_argument("-t", "--together",  
            help="Do not separate results by files", action="store_true")
    args = parser.parse_args()
    # Load main operators
    from config import config
    uiOperator = TextUIOperator(config)
    analysisOperator = AnalysisOperator(config)
    fileNames = GetFileNames(args)
    # Read files
    df = None
    for fileName in fileNames:
        with FileReader(fileName) as fileReader:
            analysisOperator.AnalyseFile(fileReader.Read(), fileName)
    if(args.together):
        df = analysisOperator.GetMergedData()
    else:
        df = analysisOperator.DataframeDict
    uiOperator.PrintData(df)
    # Make a plot on user request only
    if (args.plot):
        plotOperator = PlotOperator(config)
        plotOperator.Plot(df)

