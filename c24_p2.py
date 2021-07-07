# assign the filename
filename = "characters.txt"

# open file for writing
fileHandler = open(filename, "w")

# add some text via user input
charname = input('Please select a character name: ')
fileHandler.write(charname)

# close the file
fileHandler.close()

# open the file for reading
fileHandler = open(filename, "r")

# read a file line by line
for line in fileHandler:
    print(line)

# close the file
fileHandler.close()

