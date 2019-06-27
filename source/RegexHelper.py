import re

def GetWords(phrase):
    """ Returns a list of words from a string, removes numbers """
    regex = r'\w+'
    listToFilter = re.findall(regex,phrase.lower())
    filteredList = []
    #Remove numbers
    for word in listToFilter:
        if re.match("^\d+$", word) is None:
            filteredList += [word]
    return filteredList
