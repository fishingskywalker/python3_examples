
# define a name set
names = ["Dog", "Cat", "Mouse", "Fish"]

# add a new name
pet = "Penguin"
names.append(pet)

# print the set values
print(names)

message = "Name not found."

# take a name value for search
search_name = input("Enter a name: ")

# search the name in the set
for val in names:
    if val == search_name:
        message = "Name has been found!"
        break

print(message)
