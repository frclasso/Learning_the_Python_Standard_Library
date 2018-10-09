#Least to Greatest
pointsInGame = [0,-10,15,-2,1,12]
print(sorted(pointsInGame))

# Alphabetically
children =['Sue', 'Jerry','Linda']
print(sorted(children))

# key parameters

print(sorted("My favorite child is Linda".split(), key=str.upper))

# reverse
print(sorted(pointsInGame, reverse=True))

leaderBoard = {231:'CKL', 123:'ABC', 432:'JKC'}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))
print(leaderBoard[432])

students = [('alice','B', 12), ('eliza', 'A', 16), ('tony','C', 15)]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students,key=lambda student:student[1]))
print(sorted(students , key=lambda student:student[2]))