import numpy as np

f = open('input.txt', 'r')

file_lines = f.readlines()

ii = 0 

groups = []

entry = []

while ii < len(file_lines):
    if file_lines[ii] != '\n':
        entry.append(file_lines[ii].strip('\n'))
        if ii == len(file_lines)-1:
            groups.append(entry)
            ii += 1
        else:
            ii += 1
    elif file_lines[ii] == '\n':
        groups.append(entry)
        entry = []
        ii += 1

# set group
ans_num = []

for group in groups:
    collect = ''.join(group)
    unique = ''.join(set(collect))
    ans_num.append(len(unique))

print("Sum of all the counts: ", sum(ans_num))

# part two: all the inclusive answers

ans_num = []

for group in groups:
    people = len(group)
    if people == 1:
        collective_ans = len(group[0])
        ans_num.append(collective_ans)
    else:
        collect = ''.join(group)
        unique = ''.join(set(collect))
        for letter in unique:
            instances = collect.count(letter)
            if instances == people:
                ans_num.append(1)

print('Sum questions to which everyone answered "yes": ', sum(ans_num))
