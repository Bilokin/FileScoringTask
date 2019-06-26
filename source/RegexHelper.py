import re

def GetWords(phrase):
    regex = r'\w+'
    return re.findall(regex,phrase.lower())
