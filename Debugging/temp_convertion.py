
# Task 3
# The following program converts a range of Fahrenheit temperature readings
# to Celsius and vice versa. It begins by allowing the user to choose between
# an “F” for Fahrenheit to Celsius conversion or “C” for Celsius to Fahrenheit conversion.
# The program will print out the chosen conversions from the start value to the end value (inclusive).
# The formula for converting Fahrenheit to Celsius is:
#        C = 5/9 x ( F – 32 )
# The formula for converting Celsius to Fahrenheit is:
#        F = 32 + ( C * 9/5 )


def displayWelcome():
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit\n")

def getConvertTo():
    which = input("Enter selection:")  #1: Syntax error, did not close the string
    while which != "F" or which != "C":   #2: Logic error, should check if neither "F" nor "C" was caught
        which = input("Enter selection: ")   #3: Sytanx error, indentation error
    return which

def displayFahrenToCelsius(start, end):
    print("\n Degrees", " Degrees")
    print("Fahrenheit", "Celsius")

    for temp in range(start, end + 1):
        converted_temp = (temp - 32) * 5/9   #5: Logic error, ccalculation was incorrect as formula lacked bracket
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp))   #4: Logic error, did not call back "converted_temp"

def displayCelsiusToFahren(start, end):
    print("\n Degrees", "Degrees")
    print(" Celsius", "Fahrenheit")

    for temp in range(start, end+1):  #6: Logic error, range must be to end+1
        converted_temp = 9/5 * temp + 32   #7: Logic Error, calculation was incorrect
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp))

# --- main

#Display program welcome
displayWelcome()

# Get which conversion from user
which = getConvertTo()   #8: Logic Error, variable should be assigned to "which" for callback

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: "))  #9: Logic error, temperature should be in integer and not string

# Display range of converted temperatures
if which == "F":
    displayCelsiusToFahren(temp_start, temp_end)
elif which == "C":      #10: Logic Error, should check for "C" instead of "c"
    displayFahrenToCelsius(temp_start, temp_end)


# Open the file TEMPCONV_BUGS.py
# Save the file as TEMPCONV_DEBUG__
# 12 Identify and correct the errors in the program so 
# that it works correctly according to the rules above.
# [10]
# Save your program.
