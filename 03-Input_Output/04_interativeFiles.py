#!/usr/bin/env python3

# # Interative files

myFile = open('scores.txt', 'r')

# # Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0)

# # Iterate through each line of a file
for line in myFile:
    newHighScore = line.replace("First Player", 'Fabio')
    print(newHighScore)

myFile.close()