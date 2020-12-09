import numpy as np

f = open('input.txt', 'r')

rules = []

for rule in f.readlines():
    rules.append(rule.strip('\n'))

# part 1 

allrules = {}    
contains_shiny_gold = []

for rule in rules:
    outerbag = rule.split(' contain ')[0]
    innerbags = rule.split(' contain ')[1] 
    
    allinner = []
    for inner in innerbags.split(', '):
        allinner.append(inner.split(' ')[1] + ' ' + inner.split(' ')[2])
    allrules[outerbag[:-5]] = allinner
    
    if "shiny gold" in innerbags:
        contains_shiny_gold.append(outerbag[:-5])



# run the loop multiple times to check, if necessary

# there's probably a mathematical way to estimate the number 
# of super sets that can contain the subsets (it has to be at least 
# fewer or equal to the number of bags) but to be lazy I'll run it 
# ten times through.

lencounter = []

for ii in range(10):
    for key in allrules.keys():
        for bag in contains_shiny_gold:
            if bag in allrules[key]: 
                if key not in contains_shiny_gold:
                    contains_shiny_gold.append(key)      
                    lencounter.append(len(contains_shiny_gold))
                    print(lencounter)
    if lencounter[ii] == lencounter[ii-1]:
        break

# part 2

# to be continued...
