
# declare an ice cream list
ice_cream = ["Vanille",
             "Chocolate",
             "Strawberry"]
print("The ice cream list before any modification: ")
print(ice_cream)

# insert a new flavvor in the 3rd postion
ice_cream.insert(2, "Coffee")

# displaying list after inserting
print("The ice cream list after inserting a new flavor: ")
ice_cream.sort()
print(ice_cream)

# now remove a flavor
ice_cream.remove("Strawberry")

# print the list after the delete
print("The ice cream list after the delete: ")
ice_cream.sort()
print(ice_cream)

