import numpy as np

entries = np.genfromtxt('input.txt',dtype='str')

# part 1, check the passwords

validpasswords = []

for entry in entries:
    lettermin = float(entry[0].split('-')[0])
    lettermax = float(entry[0].split('-')[1])
    letter = entry[1].strip(':')
    password = entry[2]

    if letter in password:
        if password.count(letter) >= lettermin and password.count(letter) <= lettermax:
            validpasswords.append(password)
    else:
        pass

print('Number of valid passwords: ', len(validpasswords))

# part 2, new rules
# this became quite the mess!

newvalid = []

for entry in entries:
    lettermin = int(entry[0].split('-')[0])
    lettermax = int(entry[0].split('-')[1])
    letter = entry[1].strip(':')
    password = entry[2]
    # check to see if password is long enough at all
    if len(password) < lettermin:
        continue
    if len(password) < lettermax:
        # only check first position
        if password[lettermin-1] == letter:
            newvalid.append(password)
            continue
    if len(password) >= lettermax:         
        if (password[lettermin-1] == letter and password[lettermax-1] != letter) or (password[lettermax-1] == letter and password[lettermin-1] != letter):
            newvalid.append(password)

print("Number of valid passwords in new rule: ", len(newvalid))
