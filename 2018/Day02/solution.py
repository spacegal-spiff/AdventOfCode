from __future__ import print_function
import numpy as np

### Part 1 ###

def checksum(list_of_strings):
    """
    Advent of Code, Day 02. For a list of strings (IDs), checks whether any letters within the
    strings occur exactly twice or exactly three times. If they do, keep track with counters, 
    then sum the total number of IDs matching either criterion and multiply the two to get a 
    checksum.
    """
    # define lists of 2's and 3's
    exactlytwice = []
    exactlythrice = []

    # make list of relevant letters
    for idx,id in enumerate(list_of_strings):
        letters_to_check = list(id)
        
        # add to tracker iff no other letter satisfies criteria
        for letter in letters_to_check:
            if (id.count(letter) == 2) and (len(exactlytwice) == idx):
                exactlytwice.append(1)
            elif (id.count(letter) == 3) and (len(exactlythrice) == idx):
                exactlythrice.append(1)
            else:
                pass
        
        # if no letters satisfy 2 or 3 criteria, then append zeros for that ID
        if len(exactlytwice) == idx:
            exactlytwice.append(0)
        if len(exactlythrice) == idx:
            exactlythrice.append(0)

    return np.sum(exactlytwice)*np.sum(exactlythrice)                
            

inputstrings = np.genfromtxt('input.txt', dtype='str') 


### Part 2, the brute force method that works ###

def boxcheck2(list_of_strings):
    """
    Advent of Code, Day 02. This isn't very fast or elegant, but it works. 
    Just test strings for similarity element-wise, which provides positional matches.
    Strings differing by one element should produce a match in the overlap offset in length 
    by one element.
    """

    similarstrings = []

    for teststring in list_of_strings:
        for comparestring in list_of_strings:
            if teststring == comparestring:
                pass
            else:
                match0 = list(teststring)
                match1 = list(comparestring)

                same = []
                different = []

                for idx,letter0 in enumerate(match0):
                    if letter0 == match1[idx]:  
                        same.append(letter0)
                
                if len(same) == (len(match0) - 1):
                    print("Same is:", ''.join(same))




### Not a solution Part 2, the version that DOESN'T QUITE work ###

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def boxcheck(list_of_strings):
    """
    N.B. This doesn't work! But I'm keeping it around for reference anyway as a curiosity.
    Advent of Code, Day 02. This is a very inelegant method but it sort of gets
    the job done. Use a string matching algorithm to evaluate similarity (using the  
    Ratcliff-Obershelp algorithm built into python's difflib library) and then once 
    some matches exist, check them element-wise.
    """
    matches = []

    for idx, id in enumerate(list_of_strings):
        for jj in list_of_strings:
            if 0.95 < similar(id, jj) < 1.0:
                print(id, jj)
                matches.append([id, jj])

    similarletters = []

    for match in matches:
        match0 = list(match[0])
        match1 = list(match[1])

        same = []
        different = []

        for letter0 in match0:
            for letter1 in match1:
                if letter0 == letter1:
                    same.append(letter0)
                elif letter0 != letter1:
                    different.append([letter0, letter1])

        similarletters.append(same)
        print("Same is:", ''.join(same))

