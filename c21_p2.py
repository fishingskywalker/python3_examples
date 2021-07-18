
# define the string
string = 'There is something in my root beer.'
print("The phrase is:",string,sep='\n')

# define the search string
search = 'root'

# store the count value
count = string.count(search)

# print the formatted output
print("The search term '%s' appears %d times." % (search, count))

