
print("This program will convert a height given meters to a height given in feet and inches.")
meters = float(input("Enter height in meters:"))
meters_in_ft = int(meters // .3048)
meters_in_in = int(meters_in_ft % 12)
inches = int(meters / .3048 % 1 * 12)
print("The height is", meters_in_ft,"feet and",inches, "inches")

