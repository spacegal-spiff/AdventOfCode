import numpy as np

rucksacks = np.genfromtxt('input.txt',dtype=str)

priorities = 0

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper = [x.upper() for x in lower]

lower = np.array(lower)
upper = np.array(upper)

vals = np.concatenate([lower,upper])

for a in rucksacks:
    comp1 = a[0:int(len(a)/2)]
    comp2 = a[int(len(a)/2):]

    for thing in comp1:
        if thing in comp2:
            priority = np.where(vals == thing)[0][0] + 1
    priorities += priority


print('sum priorities:', priorities)


# part 2

badges = 0

group_idx = np.arange(0, len(rucksacks),3)

for idx in group_idx:
    elf1 = rucksacks[idx]
    elf2 = rucksacks[idx+1]
    elf3 = rucksacks[idx+2]

    for thing in elf1:
        if (thing in elf2) and (thing in elf3):
            priority = np.where(vals == thing)[0][0] + 1
    
    badges += priority


print('sum badges:', badges)
