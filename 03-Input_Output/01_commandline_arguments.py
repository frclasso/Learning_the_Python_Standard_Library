#!/usr/bin/env python3

import sys

# Usage: On terminal, python3 01_commandline_arguments 1 2 3
# First argument is the name

## Print arguments
print("Number of arguments: ", len(sys.argv), 'arguments.')
print('Arguments: ', sys.argv)

print()
## Removing arguments
sys.argv.remove(sys.argv[0])
print('Now the arguments are: ', sys.argv)
print("Number of arguments:", len(sys.argv), 'arguments.')

## Sum up the arguments

arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")
print(sum)