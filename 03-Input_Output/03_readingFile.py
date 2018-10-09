# Read the file
myFile = open('scores.txt', 'r')
print("Reading...\n" + myFile.read(17))
myFile.seek(0) # retorna o cursor para i inicio
print("Reading again...\n" + myFile.read(17))