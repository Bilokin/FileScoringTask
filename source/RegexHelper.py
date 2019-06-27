#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def GetWords(phrase):
    """ 
    Returns a list of words from a string, removes numbers 
    Args:
        phrase (str): String to parse
    Returns: 
        (list) list of words
    """
    regex = r'\w+'
    listToFilter = re.findall(regex,phrase.lower())
    filteredList = []
    #Remove numbers
    for word in listToFilter:
        if re.match("^\d+$", word) is None:
            filteredList += [word]
    return filteredList
