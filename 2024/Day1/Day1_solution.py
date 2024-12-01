import numpy as np

# part 1!
a, b = np.genfromtxt('input.txt').T

dists = np.sum(abs(np.sort(a) - np.sort(b)))

print("Part 1 solution:", int(dists))


# part 2!
score = []

for number in a:
    occ = list(b).count(number)
    score.append(occ*number)

print("Part 2 solution:", int(np.sum(score)))

