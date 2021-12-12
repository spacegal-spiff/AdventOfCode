import numpy as np

depths = np.genfromtxt('input.txt')

# Part 1
count = 0 

for idx,meas in enumerate(depths):
    if idx < len(depths)-1:
        if depths[idx + 1] > meas:
            count += 1

print(count)

# Part 2

def slidingcalc(data, window):
    """
    Function to calculate sliding window of arbitrary size.
    Input data should be a 1D array. 
    Window should be an integer.
    Output is an array of binned values.
    """
    n = len(data)
    vals = []
    for ii in range(n - (window - 1)):
        newval = np.sum(data[ii:ii+window])
        vals.append(newval)

    return vals
         
binned = slidingcalc(depths,3)

binnedcount = 0

for idx,meas in enumerate(binned):
    if idx < len(binned)-1:
        if binned[idx + 1] > meas:
            binnedcount += 1

print(binnedcount)    
