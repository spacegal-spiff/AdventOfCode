import numpy as np

f = open('input.txt', 'r')

file_lines = f.readlines()

ii = 0

passports = []

entry = []

while ii < len(file_lines):
    if file_lines[ii] != '\n':
        entry.append(file_lines[ii].strip('\n'))
        ii += 1
    else:
        passports.append(entry)
        entry = []
        ii += 1

criteria = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = []

for entry in passports:
    
    validate = []
    
    for criterion in criteria:
        if True in [criterion in x for x in entry]:
            validate.append(1)
    
    if sum(validate) == len(criteria):
        valid.append(entry)            
              

