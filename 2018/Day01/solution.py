from __future__ import print_function
import numpy as np

### Part 1 ###

def simplesum(x):
    """
    Advent of Code, Day 01. This one, uh, "does what it says on the tin."
    """

    total = 0
    for element in x:
        total += element
    return total


values = np.loadtxt('input.txt')

print("Estimated sum is:", simplesum(values))




### Part 2, take 1, the impossibly slow version ###

import itertools

def checkfreq(x, verbose=True):
    """
    Advent of Code, Day 01. Uses itertools to cycle through a list of values, adding one 
    element at a time to a running total, until a summed value is reached twice. Impossibly slow 
    (I think) due to list operations, so determining whether the running total array is unique by 
    comparing how many unique values were expected is... not advisable.
    """

    total = 0
    idx = 0
    runningsum = [0]

    cyclex = itertools.cycle(x)

    while True: 
        total += next(cyclex)
        runningsum.append(total)

        idx += 1
        
        if verbose==True:
            print("Running sum:", runningsum)
            print("Unique values:", np.unique(runningsum))
            print("idx:", idx)

        # check every 1000th index for a progress report 
        if idx % 1000 == 0:
            print("Index checkpoint: " , idx)
            print("Length of running sum:", len(runningsum))
            print("Length of unique values:", len(np.unique(runningsum)))


        if len(np.unique(runningsum)) < len(runningsum):
            print("Encountered duplicate!")
            print("Duplicated at position ", idx, " and reached value of", runningsum[-1], "twice.")
            break



### Part 2, take 2: now MUCH FASTER with DICTIONARIES ###

def checkfreq_dict(x, verbose=True):
    """
    Advent of Code, Day 01. A lot like checkfreq, but it turns out checking whether a key exists in
    a dictionary is an outrageously faster (< 1 sec vs. > 25 min) operation than using np.unique 
    on an array. 
    """

    total = 0
    idx = 0
    runningsum = {0:[]}

    cyclex = itertools.cycle(x)

    while True: 
        total += next(cyclex)

        idx += 1
        
        if verbose==True:
            print("Running sum:", runningsum)
            print("Unique values:", np.unique(runningsum))
            print("idx:", idx)

        # check every 1000th index for a progress report 
        if idx % 1000 == 0:
            print("Index checkpoint: " , idx)

        if total in runningsum:
            print("Encountered duplicate!")
            print("Duplicated at position ", idx, " and reached value of", total, "twice.")
            break

        runningsum[total] = []



