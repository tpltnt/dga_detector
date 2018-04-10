# Helpful DGA and string randomness detection routines
import math
import re


def entropy(string):
    """
    Calculates the Shannon entropy of a string.

    :param string: input string
    :type string: str
    :returns: float
    """

    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy


def count_consonants(string):
    """
    Counting consonants in a string.

    :param string: input string
    :type string: str
    :retuns: int (number of consonants)
    """
    consonants = re.compile("[bcdfghjklmnpqrstvwxyz]")
    count = consonants.findall(string)
    return len(count)

