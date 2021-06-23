# Define a dictionary
customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali',
'02834':'Mosarof Ahmed','05623':'Mila Hasa', '07895':'Yqub Ali'}

# Append a new data
customers['05634'] = 'Mehboba Ferdous'

print("The customer names are:")
# Print the values of the ditionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
name = input("Enter customer ID:")

# Search the ID in the dictionary
for customer in customers:
    if customer == name:
        print(customers[customer])
        break

