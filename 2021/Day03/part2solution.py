# Day 03
import numpy as np

vals = np.loadtxt('input.txt', dtype=str)

array = np.zeros([len(vals), len(vals[0])])

gammarate = np.zeros(len(vals[0]))
epsilonrate = np.zeros(len(vals[0]))

for idx,val in enumerate(vals):
    elements = list(val)
    array[idx,:] = np.array([int(x) for x in elements])

gamma = np.sum(array, axis = 0)

# Part 2

oxy = []


if len(vals) > 1:
    for idx in range(12):
        element = gamma[idx]
        print(element)
        if element >= len(vals)/2.:
            for val in vals:
                if val[idx] == '1':
                    oxy.append(val)
            if len(oxy) > 0:
                print(f'length {len(oxy)} at bit {idx}')
            vals = oxy
            oxy = []
        if element < len(vals)/2.:
            for val in vals:
                if val[idx] == '0':
                    oxy.append(val)
            vals = oxy
            oxy = []
            if len(oxy) > 0:
                print(f'length {len(oxy)} at bit {idx}')
        
        array = np.zeros([len(vals), len(vals[0])])

        for idx,val in enumerate(vals):
            elements = list(val)
            array[idx,:] = np.array([int(x) for x in elements])

        gamma = np.sum(array, axis = 0)
        # print(gamma)
        if len(vals) == 1:
            final_oxy = int(vals[0],2)
            print('done! oxygen:', vals[0], int(vals[0],2))

        

#rinse and repeat for co2

vals = np.loadtxt('input.txt', dtype=str)

array = np.zeros([len(vals), len(vals[0])])

gammarate = np.zeros(len(vals[0]))
epsilonrate = np.zeros(len(vals[0]))

for idx,val in enumerate(vals):
    elements = list(val)
    array[idx,:] = np.array([int(x) for x in elements])

gamma = np.sum(array, axis = 0)

co2 = []

if len(vals) > 1:
    for idx in range(12):
        element = gamma[idx]
        print(element)
        if element >= len(vals)/2.:
            for val in vals:
                if val[idx] == '0':
                    co2.append(val)
            if len(co2) > 0:
                print(f'length {len(co2)} at bit {idx}')
            vals = co2
            co2 = []
        if element < len(vals)/2.:
            for val in vals:
                if val[idx] == '1':
                    co2.append(val)
            vals = co2
            co2 = []
            if len(co2) > 0:
                print(f'length {len(co2)} at bit {idx}')
        
        if len(vals) > 1:
            array = np.zeros([len(vals), len(vals[0])])

            for idx,val in enumerate(vals):
                elements = list(val)
                array[idx,:] = np.array([int(x) for x in elements])

            gamma = np.sum(array, axis = 0)
        # print(gamma)
        if len(vals) == 1:
            final_co2 = int(vals[0],2)
            print('done! co2:', vals[0], int(vals[0],2))

print("final product: ", final_co2*final_oxy)