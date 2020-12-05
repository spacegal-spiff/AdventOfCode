import numpy as np

f = open('input.txt', 'r')

file_lines = f.readlines()

# Part 1 

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
    
    validate = 0
    
    for criterion in criteria:
        if True in [criterion in x for x in entry]:
            validate += 1
    
    if validate == len(criteria):
        valid.append(entry) 

print("Number of valid passports in Part 1: ", len(valid))                   
              
# Part 2

finalvalidate = []

for entry in passports:
    validate = []
    newvalid = 0

    for criterion in criteria:
        if True in [criterion in x for x in entry]:
            validate.append(1)

    if sum(validate) == len(criteria):
        lookup = {}

        for part in entry:
            fields = part.split(' ')
            for field in fields:
                k = field.split(':')[0]
                v = field.split(':')[1]
                lookup[k] = v


        if int(lookup['byr']) >= 1920 and int(lookup['byr']) <= 2002:
            newvalid += 1

        if int(lookup['iyr']) >= 2010 and int(lookup['iyr']) <= 2020:
            newvalid += 1

        if int(lookup['eyr']) >= 2020 and int(lookup['eyr']) <= 2030:
            newvalid += 1

        if ('cm' in lookup['hgt'] and int(lookup['hgt'].strip('cm')) >= 150 and int(lookup['hgt'].strip('cm')) <= 193) or ('in' in lookup['hgt'] and int(lookup['hgt'].strip('in')) >= 59 and int(lookup['hgt'].strip('in')) <= 76):
            newvalid += 1

        if ('#' == lookup['hcl'][0]) and (len(lookup['hcl']) == 7):
            newvalid += 1

        if lookup['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            newvalid += 1

        if len(lookup['pid']) == 9:
            newvalid += 1

    if newvalid == 7:
        finalvalidate.append(entry)


print("Final valid passports: ", len(finalvalidate))

