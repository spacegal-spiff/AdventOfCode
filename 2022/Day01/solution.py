import numpy as np


with open('input.txt') as f:
    lines = f.readlines()

calories = 0
max_calories = 0
calorie_count = []

for idx,line in enumerate(lines):
    if line != '\n' and idx != len(lines)-1:
        calories  += int(line.strip('\n'))
    elif line == '\n':
        calorie_count.append(calories)
        if calories > max_calories:
            max_calories = calories
            calories = 0
        else:
            calories = 0
    else:
        calories  += int(line.strip('\n'))
        calorie_count.append(calories)

print("Max calories: ", max_calories)

# sort calories
calorie_count.sort()

print("Top three max calories: ", calorie_count[-3:])

print("Sum of top three max calories: ", np.sum(calorie_count[-3:]))


