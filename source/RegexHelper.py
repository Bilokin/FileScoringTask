#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def GetWords(phrase):
    """ 
    Returns a list of words from a string, removes numbers 
    Args:
        phrase (str): String to parse
    Returns: 
        filteredList (list): list of words
    """
    # Remove special characters regex
    # It works faster than the standard \w+ pattern
    regex = re.compile(r'([^\d\`\~\!\@\#\$\%\^\&\*\(\)\+\=\[\{\]\}\|\\\'\<\,\.\>\?\/\""\;\:\s]+)+',
            re.UNICODE)
    return re.findall(regex,phrase.lower())
