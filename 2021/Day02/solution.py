# Day 02
import numpy as np

# Part 1

move, val = np.genfromtxt('input.txt', dtype='str').T

val = np.array([float(x) for x in val])

motion = 0

depth_old = 0

depth = 0 

aim = 0

for idx,command in enumerate(move):
    if command == 'forward':
        motion += val[idx]
        depth += aim*val[idx]
    elif command == 'down':
        depth_old += val[idx]
        aim += val[idx]
    else:
        depth_old -= val[idx]
        aim -= val[idx]

print("Part1: Motion = ", motion, ", Depth = ", depth_old, ", Product: ", motion*depth_old)   

print("Part2: Motion = ", motion, ", Depth = ", depth, "Product: ", motion*depth)

# Part 2

