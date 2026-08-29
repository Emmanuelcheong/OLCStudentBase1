
# Task 3
# The following program should read a denary non-negative integer from the user. 
# The program will then convert the denary integer to its 
#    binary value and print it to the screen. 
# The “division by 2” method is employed to carry out the conversion. 
# There are several syntax errors and logical errors in the program.

NEW_BASE = 2  #1: Syntax error, "==" should be "="     2: Logic Error, "NEW_BASE" should be 2 instead of 3
num = input("Enter a non-negative integer: ") #3: Syntax Error, no close bracket   #4:Syntax Error, should be "input" instead of "Input"
num = int(num)     #5: Logic Error, should be converted to integer and not float
result = ""
q = num
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE
while q > 0:    #6: Syntax Error, no ":" for while loop
    r = q % NEW_BASE
    result =  str(r) + result #7: Logic error, concatenation of variables in wrong order
    q = q // NEW_BASE    #8: Logic error, should be floor division
print(num, "in Decimal is", result, "in Binary.")   #9: Logic error, print statement should show final answer   #10: Logic Error, order of variables is wrong

# Open the file D2B.py
# Save the file as MYD2B___
# 
# Identify and correct the errors in the program so that it 
# works correctly according to the description above. Save your program.
#  [10] 