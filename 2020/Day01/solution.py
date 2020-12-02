import numpy as np

# note to the curious reader:
# someday I will (not likely) fix the superfluous print statements

values = np.genfromtxt('input.txt')

# part one

for entry in values:
    if len(np.argwhere(values+entry == 2020)) > 0:
        matching_val = values[np.where(values+entry==2020)]
        print('value is: ', entry)
        print('matching value is: ', matching_val)

        print('pair multiplied: ', matching_val * entry)

# part two - sum of THREE entries!

# this is less than elegant

for entry in values:
    for entry2 in values:
        if len(np.argwhere(values+entry+entry2 == 2020)) > 0:
            val1 = values[np.where(values+entry+entry2 == 2020)]
            print('values are: ', entry, entry2)
            print('matching value is: ', val1)

            print('trifecta, multiplied: ', val1*entry*entry2)

