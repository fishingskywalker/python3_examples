# this script is not ideal for try & except
# this was just an excercise in random scripting

# try block
try:
    # input a name
    charname = str(input('Enter a name: '))
    print("The name has ",len(charname)," characters.")
    if len(charname) % 2 == 0:
        print("The name has an even number of characters.\n")
    else:
        print("The name has an odd number of characters.\n")

# exception block
except (ValueError):
    # print error message
    print("Enter a name that uses letters only")

