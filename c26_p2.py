# import the pickle module
import pickle

# declare the object to store data
dataObject = []
# iterate the loop for 5 times
for num in range(10,20):
    dataObject.append(num)

# open a file for writing data
file_handler = open('counting', 'wb')
# dump the data of the object into the file
pickle.dump(dataObject, file_handler)
# close the file handler
file_handler.close()

# open a file for reading the file
file_handler = open('counting', 'rb')
# load the data from the file after deserialization
dataObject = pickle.load(file_handler)
# iterate the loop to print the data
for val in dataObject:
    print(' The data value : ', val)

# close the file handler
file_handler.close()

