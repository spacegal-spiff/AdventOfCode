import numpy as np

# read in input as separate arrays
you, me = np.genfromtxt('input.txt', dtype='str').T

# define numeric translation dictionary
points = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2,'Z':3}

win = 6
draw = 3

running_score = 0 

# part 1
for idx, choice in enumerate(me):
    if me[idx] == 'X': # rock 
        if you[idx] == 'B': # paper
            score = points['X']
        elif you[idx] == 'C': # scissors
            score = win + points['X']
        else:
            score = draw + points['X']

    if me[idx] == 'Y': # paper
        if you[idx] == 'A': # rock
            score = win + points['Y']
        elif you[idx] == 'C': # scissors
            score =  points['Y']
        else:
            score = draw + points['Y']

    if me[idx] == 'Z': # scissors
        if you[idx] == 'A': # rock
            score = points['Z']
        elif you[idx] == 'C': # scissors
            score =  draw + points['Z']
        else:
            score = win + points['Z']

    running_score += score



# part 2

running_score = 0

for idx, choice in enumerate(me):
    if me[idx] == 'X': # need to lose 
        if you[idx] == 'B': # paper
            score = points['X']
        elif you[idx] == 'C': # scissors
            score = points['Y']
        else:
            score = points['Z']

    if me[idx] == 'Y': # need to draw
        if you[idx] == 'A': # rock
            score = draw + points['X']
        elif you[idx] == 'C': # scissors
            score = draw +  points['Z']
        else:
            score = draw + points['Y']

    if me[idx] == 'Z': # need to win
        if you[idx] == 'A': # rock
            score = win + points['Y']
        elif you[idx] == 'C': # scissors
            score =  win + points['X']
        else:
            score = win + points['Z']

    running_score += score
