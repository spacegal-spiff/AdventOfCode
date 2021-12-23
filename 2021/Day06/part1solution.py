# Day 06
import numpy as np
import time

# Part 1

allfish = np.genfromtxt('input.txt', delimiter=',')

days = 80

t0 = time.time()

for ii in range(days):
    af = allfish
    af -= 1
    af[np.where(af == -1)] = 6

    if ii < days-1:
        num_newfish = np.count_nonzero(af == 0)
        newfish = np.zeros(num_newfish) + 9
        allfish = np.concatenate((af,newfish))

    """
    keeping in the agonizingly slow loops for posterity
    """
    # allfish = [x - 1 for x in allfish]
    # for idx,fish in enumerate(allfish):
    #      if fish == -1:
    #          allfish[idx] = 6
    # allfish = list(af)
    # num_newfish = allfish.count(0)
    # for ii in range(num_newfish):
    #     allfish.append(9)        


t1 = time.time()

print(f"Number of fish at day {days}: {len(allfish)}")            
print(f"Time taken: {(t1-t0)/60.} minutes.")

# Part 2
# _Apparently_ the internet says we can't keep track 
# of every 🐟, owing to O(log N) :( :( :( 

# small test scenario: for each fish, determine age at X days 
# and how many fish it spawned?
# so after x days, how many fish has fish A spawned? 



