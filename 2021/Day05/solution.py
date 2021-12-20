# Day 05

import numpy as np
import matplotlib.pyplot as plt

coords = np.genfromtxt('input.txt', delimiter = ' -> ', dtype=str)

xstart = [int(x[0].split(',')[0]) for x in coords]

xend = [int(x[1].split(',')[0]) for x in coords]

ystart = [int(x[0].split(',')[1]) for x in coords]

yend = [int(x[1].split(',')[1]) for x in coords]

# determine size of array based on largest dimension
size = max(max(xstart), max(xend), max(ystart), max(yend))


# part 1

# initialize empty array to store values
arr = np.zeros([size+1, size+1])

for idx,line in enumerate(coords):
    if xstart[idx] == xend[idx] and ystart[idx] != yend[idx]:
        print(f'Vertical line at {xstart[idx]} from {ystart[idx]} to {yend[idx]}.')
        # vertical line
        yi = min(ystart[idx], yend[idx])
        yf = max(ystart[idx], yend[idx])
        for point in np.arange(yi, yf+1,1):
            arr[point, xstart[idx]] += 1
    elif ystart[idx] == yend[idx] and xstart[idx] != xend[idx]:
        print(f'Horizontal line at {ystart[idx]} from {xstart[idx]} to {xend[idx]}.')
        # horizontal line
        xi = min(xstart[idx], xend[idx])
        xf = max(xstart[idx], xend[idx])
        for point in np.arange(xi, xf+1,1):
            arr[ystart[idx], point] += 1
    else:
        print('diagonal line!')
        

# convert crossover points to nans
arr[np.where(arr >= 2)] = np.nan

print(np.sum(np.isnan(arr)))


# part 2

# initialize empty array to store values
arr = np.zeros([size+3, size+3])

for idx,line in enumerate(coords):
    if xstart[idx] == xend[idx] and ystart[idx] != yend[idx]:
        print(f'Vertical line at {xstart[idx]} from {ystart[idx]} to {yend[idx]}.')
        # vertical line
        yi = min(ystart[idx], yend[idx])
        yf = max(ystart[idx], yend[idx])
        for point in np.arange(yi, yf+1,1):
            arr[point, xstart[idx]] += 1
    elif ystart[idx] == yend[idx] and xstart[idx] != xend[idx]:
        print(f'Horizontal line at {ystart[idx]} from {xstart[idx]} to {xend[idx]}.')
        # horizontal line
        xi = min(xstart[idx], xend[idx])
        xf = max(xstart[idx], xend[idx])
        for point in np.arange(xi, xf+1,1):
            arr[ystart[idx], point] += 1
    else:
        print(f'Diagonal line w/y from {ystart[idx]} to {yend[idx]} and x from {xstart[idx]} to {xend[idx]}.')

        xi = min(xstart[idx], xend[idx])
        xf = max(xstart[idx], xend[idx])
        yi = min(ystart[idx], yend[idx])
        yf = max(ystart[idx], yend[idx])
        xrange = np.arange(xi, xf+1, 1)
        if yend[idx] > ystart[idx] and xend[idx] > xstart[idx]:
            # positive slope
            for jj, xpoint in enumerate(np.arange(xi, xf+1,1)):
                arr[yi+jj, xpoint] += 1
        elif yend[idx] < ystart[idx] and xend[idx] > xstart[idx]:
            # negative slope
            for jj, xpoint in enumerate(np.arange(xi, xf+1,1)):
                arr[yf-jj, xpoint] += 1                   
        elif yend[idx] < ystart[idx] and xend[idx] < xstart[idx]:
            # negative slope
            for jj, xpoint in enumerate(np.arange(xi, xf+1,1)):
                arr[yf-jj, xf-jj] += 1
        else:
            # positive slope
            for jj, xpoint in enumerate(np.arange(xi, xf+1,1)):
                arr[yf-jj, xpoint] += 1                            




# convert crossover points to nans
arr[np.where(arr >= 2)] = np.nan

print(np.sum(np.isnan(arr)))

plt.imshow(arr)
plt.savefig('part2image.png')
