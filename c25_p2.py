# import os module to read directory
import os

# set the directory path with user input
path = input('Please input directory path: ')

# read the content of the variable
files = os.listdir(path)

# print the content of the directory
for file in files:
    print(file)

