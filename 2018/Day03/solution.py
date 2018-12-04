import numpy as np 


def clothoverlap(list_of_claims):
    """
    Advent of Code, Day 03. For each claim, parse the string to place the claim location and size 
    into an N-dimensional array, then sum that array to find the overlapping values.

    NOTE: The input text file has been modified to remove the hash symbol since python interprets 
    that as a comment. The original input could be used by adding:
    claim = claim.strip('#') at line 18.
    """
    dimension = len(list_of_claims)

    cloth = np.zeros([1000,1000,dimension])

    for idx,claim in enumerate(list_of_claims):
        claim_id = int(claim.split('@')[0])
        locx = int(claim.split('@')[1].split(':')[0].split(',')[0])
        locy = int(claim.split('@')[1].split(':')[0].split(',')[1])
        sizex = int(claim.split('@')[1].split(':')[1].split('x')[0])
        sizey = int(claim.split('@')[1].split(':')[1].split('x')[1])

        cloth[locy:locy+sizey, locx:locx+sizex, idx] = 1.0

    totalclaims = cloth.sum(axis=2)

    return totalclaims


### Part 1 ###

claimlist = np.genfromtxt('input.txt', dtype='str', delimiter='\n')

totalclaims = clothoverlap(claimlist)

solution = len(totalclaims[np.where(totalclaims >=2.0)])


### Part 2 ###


def singlecloth(list_of_claims, totalclaims):
    """
    Advent of Code, Day 03. Part 2 requires a small modification to the function above in 
    order to determine where the final cloth has a single contiguous claim with no 
    overlapping pieces. In this case, take the final summed output, wherein any "single" 
    claims will have value unity. Then evaluate whether a given claim "slice" in the N-dimensional 
    array is identical to that final summed output. If it is, then it's a match.

    Pondering further, I suspect clever things could be done with the final summed array to 
    search for contiguous islands of value unity. I suspect that finding the largest contiguous 
    island would lead to the correct result as well, and it looks like there are some fun approaches 
    using Kadane's algorithm to solve the maximum subarray problem:
    https://en.wikipedia.org/wiki/Maximum_subarray_problem 
    """
    dimension = len(list_of_claims)

    cloth = np.zeros([1000,1000,dimension])

    for idx,claim in enumerate(list_of_claims):
        claim_id = int(claim.split('@')[0])
        locx = int(claim.split('@')[1].split(':')[0].split(',')[0])
        locy = int(claim.split('@')[1].split(':')[0].split(',')[1])
        sizex = int(claim.split('@')[1].split(':')[1].split('x')[0])
        sizey = int(claim.split('@')[1].split(':')[1].split('x')[1])

        cloth[locy:locy+sizey, locx:locx+sizex, idx] = 1.0


        if np.sum(cloth[locy:locy+sizey, locx:locx+sizex, idx] - totalclaims[locy:locy+sizey, locx:locx+sizex]) == 0:
            print("Found swath! At location ", claim_id)

    totalclaims = cloth.sum(axis=2)

    return totalclaims


