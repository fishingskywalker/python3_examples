# Import as module to read directory
import os

# Set the directory path
path = 'C:/Users/fr0z3/Desktop/python3_examples/'

# Read the content of the file
files = os.listdir(path)

# Print the content of the directory
for file in files:
    print(file)

