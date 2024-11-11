# Jaxson Viergets
# UWYO COSC 1010
# 11/10/2024
# Lab 08
# Lab Section:12
# Sources, people worked with, help given to: Lee Huber 
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def int_or_float(string):
    """Check if the string is a integer or float then change it"""
    
    if string.lower() == "exit":
        return "exit"
    
    parts = string.split(".")
    
    if len(parts) == 2 and ((parts[0].isdigit() and parts[1].isdigit()) or (parts[0][0] == "-" and parts[0][1:].isdigit() and parts[1][0:].isdigit())):
        return float(f"{parts[0]}.{parts[1][0]}")
    
    if len(parts) == 1 and (parts[0].isdigit() or (parts[0][0] == "-" and parts[0][1:].isdigit())):
        return int(string) 

    return False
print("*" * 75)



# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def get_valid_input(prompt, input_type, is_integer=False):
    """proper collection of inputs and or values"""
    while True:
        user_input = int_or_float(input(prompt))
        if user_input == "exit":
            return "exit"
        if isinstance(user_input, input_type) and (not is_integer or isinstance(user_input, int)):
            return user_input
        print(f"Invalid input, please enter a valid {input_type.__name__}{' (integer)' if is_integer else ''}.")

def slope_intercept(b, slope, lower_bound, upper_bound):
    """Calculate and print points on the line y = mx + b for a given range."""
    for x in range(lower_bound, upper_bound + 1):
        y = (x * slope) + b
        print(f"\t({x}, {int_or_float(str(y))})")

while True:
    # Get valid inputs for b, slope, lower_bound, and upper_bound
    b = get_valid_input("Type exit to exit\nEnter b here: ", (int, float))
    if b == "exit": break

    slope = get_valid_input("Enter slope here: ", (int, float))
    if slope == "exit": break

    lower_bound = get_valid_input("Enter lower bound here (whole #'s only): ", int, is_integer=True)
    if lower_bound == "exit": break

    upper_bound = get_valid_input("Enter upper bound here (whole #'s only): ", int, is_integer=True)
    if upper_bound == "exit": break

    # Display the points on the line
    print("All numbers are in cordiantes: (y, x):")
    slope_intercept(b, slope, lower_bound, upper_bound)
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def sqrt(num):
    if num > 0:
        return (num**.5)
    else:
        return False

def quadratic(a, b, c):
    sqroot = sqrt((b**2)-4*a*c)
    if sqroot != False:
        return f"Key 1: {int_or_float(str((-b+sqroot)/(2*a)))}\nKey 2: {int_or_float(str((-b-sqroot)/(2*a)))}"
    else:
        return False

while True:
    
    a = int_or_float(input("Type exit to exit\nEnter the a vale here: "))
    if a == "exit":
        break
    while type(a) not in (int, float):
        a = int_or_float(input("Try again, enter the a value here: "))
        if a == "exit":
            break
    if a == "exit":
        break

    b = int_or_float(input("Enter the b value here: "))
    if b == "exit":
        break
    while type(b) not in (int, float):
        b = int_or_float(input("Try again, enter the b value here: "))
        if b == "exit":
            break
    if b == "exit":
        break


    c = int_or_float(input("Enter the c value here: "))
    if c == "exit":
        break
    while type(c) not in (int, float):
        c = int_or_float(input("Try again, enter the c value here: "))
        if c == "exit":
            break
    if c == "exit":
        break


    if quadratic(a, b, c) != False:
        print(quadratic(a, b, c))
    else:
        print("YO, Bro I can't do any imaginary numbers, try again with some diffrent numbers!")