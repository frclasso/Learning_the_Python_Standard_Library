#!/usr/bin/env python3

ages = [12, 19, 39, 87, 7,2]

for age in ages:
    isAdult = age > 17
    if isAdult:
        print('Being: ' + str(age) + " make you an adult")
    if not isAdult:
        print("Being: " + str(age) + " does not make you an adult.")
