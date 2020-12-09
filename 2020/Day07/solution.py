import numpy as np

f = open('test.txt', 'r')

rules = []

for rule in f.readlines():
    rules.append(rule.strip('\n'))

