import numpy as np

passes = np.genfromtxt('input.txt', dtype='str') 


def eval(minval, maxval, letter):
    if letter == 'F' or letter == 'L':
        newmin = minval
        newmax = np.floor((maxval-minval)/2) + minval
    if letter == 'B' or letter == 'R':
        newmax = maxval
        newmin = np.ceil((maxval-minval)/2) + minval   
    return newmin, newmax

def checkrow(seat):
    startmin = 0
    startmax = 127

    for ii in range(7):
        startmin, startmax = eval(startmin, startmax, seat[ii])

    return startmin

def checkcolumn(seat):
    startmin = 0
    startmax = 7

    for ii in range(7,10):
        startmin, startmax = eval(startmin, startmax, seat[ii])

    return startmin

# seatid = row*8 + column

allseatids = []
rows_columns = []

for entry in passes:
    seatid = checkrow(entry)*8 + checkcolumn(entry)
    allseatids.append(seatid)
    rows_columns.append((checkrow(entry),checkcolumn(entry),seatid))

print("Maximum seat ID: ", max(allseatids))

# part 2, find the missing seat

# need to generate a manifest
rows = np.arange(0,128,1)
columns = np.arange(0,8,1)

manifest = []

for row in rows:
    for column in columns:
        manifest.append(row*8+column)

# this is kinda slow... is there a better way I wonder?
# maybe arrays are faster than lists in this case? hmmmmmm

for seat in manifest:
    if seat not in allseatids:
        if seat+1 in allseatids and seat-1 in allseatids:
            print("your seat is ", seat, "!")
