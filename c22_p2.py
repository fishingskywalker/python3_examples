# define subtraction function
def subtract(b, a):
    result = b - a
    print("Subtraction result:",result)

# define are function with return statement
def area(radius):
    result = 3.14 * radius * radius
    return result

# call subtraction function
y = float(input("Enter the first number: "))
x = float(input("Enter the second number: "))
subtract(y, x)

# call area function
x = float(input("Enter radius of circle: "))
print("Area of the circle is",area(x))

