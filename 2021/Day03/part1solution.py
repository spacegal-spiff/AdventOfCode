# Day 03
import numpy as np

vals = np.loadtxt('input.txt', dtype=str)

array = np.zeros([len(vals), len(vals[0])])

gammarate = np.zeros(len(vals[0]))
epsilonrate = np.zeros(len(vals[0]))

# generate a 2D array so we can slice it
# hope this isn't a bad life choice for part 2
for idx,val in enumerate(vals):
    elements = list(val)
    array[idx,:] = np.array([int(x) for x in elements])

gamma = np.sum(array, axis = 0)

for ii in range(len(gammarate)):
    if gamma[ii] > len(vals)/2.:
        gammarate[ii] = 1
    elif gamma[ii] < len(vals)/2.:
        gammarate[ii] = 0
    else:
        print('equal number of zeros and ones?!')

epsilonrate = gammarate + 1

epsilonrate[epsilonrate == 2] = 0

## convert from binary into decimal
# first convert array into joined string
gam = ''.join([str(int(x)) for x in gammarate])
# then niftily use python dtypes to do your bidding
gam = int(gam,2)

eps = ''.join([str(int(x)) for x in epsilonrate])
eps = int(eps,2)

print('binary values for gamma, epsilon: ', gammarate, epsilonrate)
print('gamma: ', gam, ', epsilon = ', eps, ', product = ', gam*eps)

# spoiler alert, that was not a wise way to code this in prep for part 2
