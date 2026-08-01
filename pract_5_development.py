
############################################################
# TASK 5 - HOLIDAY WORKSHOP BOOKING SYSTEM
############################################################

# A school is organising several holiday workshops.
# The school requires a program to create and store for workshop bookings.

# Open a new JupyterLab notebook and save it as:
# TASK5_.ipynb

# For each sub-task, add a comment using the hash symbol '#'
# at the beginning of your code to indicate the sub-task that the program code belongs to.

# For example:
# # Task 5.1
# Program Code

# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# The following workshops and fees are available:
# ROB - Robotics - $48.00 per student
# WEB - Web Design - $36.00 per student
# PYT - Python Programming - $42.00 per student

# You can assume that a parent's name contains at least
# three characters.

############################################################
# Task 5.1 [4]
############################################################

# Write a function valid_workshop_code() that:

# - takes workshop_code as a parameter;
# - checks that the workshop code contains exactly three characters;
# - checks that the workshop code is ROB, WEB or PYT;
# - accepts the workshop code regardless of letter case;
# - returns True if the workshop code is valid or False  otherwise.
# - Display the appropriate reason for non valid workshop codes.

# Save your program.
# Task 5.1 
#______________________________________________________________
# def valid_workshop_code(workshop_code):
#     valid = ["ROB", "WEB", "PYT" ] # valid workshop codes

#     if len(workshop_code) != 3: # checking valid length
#         print("Workshop code must contain exactly three characters")
#         return False
#     elif workshop_code.upper() not in valid:  
#         print("workshop code must be ROB, WEB or PYT")
#         return False
#     else:
#         # if code comes here, means its valid.
#         return True


# print(valid_workshop_code("pyt"))
# print(valid_workshop_code("pydt"))
# print(valid_workshop_code("web"))










############################################################
# Task 5.2 [4]
############################################################

# Copy and paste your program from sub-task 5.1.

# Extend the program by writing a function
# calculate_booking_fee() that:

# - takes workshop_code (string) and number_of_students (integer) as parameters;
# - calculates the total fee using the appropriate fee per student;
# - deducts a discount of 10% if three or more students are included in the booking;
# - returns the total booking fee.

# You can assume that workshop_code and number_of_students are valid.
# ROB - Robotics - $48.00 per student
# WEB - Web Design - $36.00 per student
# PYT - Python Programming - $42.00 per student
# Save your program.
# Task 5.2 
#______________________________________________________________

def valid_workshop_code(workshop_code):
    valid = ["ROB", "WEB", "PYT" ] # valid workshop codes

    if len(workshop_code) != 3: # checking valid length
        print("Workshop code must contain exactly three characters")
        return False
    elif workshop_code.upper() not in valid:  
        print("workshop code must be ROB, WEB or PYT")
        return False
    else:
        # if code comes here, means its valid.
        return True
def calculate_booking_fee(workshop_code, number_of_students):
    workshop_code = workshop_code.upper() # allow for  code to not be case sensitive
    total = 0 # total cost
    pricing = 0  # cost of each different workshop code
    if workshop_code == "ROB":
        pricing = 48
    elif workshop_code == "WEB":
        pricing = 36
    else:
        pricing = 42
    total = pricing * number_of_students   #calculate the total for all students
    if number_of_students >=3:
        total = total * 0.9   # discount if theres 3 or more students
    return total  #returns the total















############################################################
# Task 5.3 [2]
############################################################

# Copy and paste your program from sub-task 5.2.

# Extend the program by writing a function
# create_booking_reference() that:

# - takes parent_name and workshop_code as parameters;
# - generates a random six-digit booking number from 100000 to 999999 inclusive;
# - creates a booking reference containing:
#     - the first three characters of the parent's name in uppercase;
#     - the workshop code in uppercase;
#     - the six-digit booking number;
# - returns the booking reference.

# For example:
# Parent name: Siti
# Workshop code: pyt
# Random booking number: 583104
# Booking reference: SITPYT583104

# Save your program.
# Task 5.3
#______________________________________________________________
# import random #Allows for random numbers
# def create_booking_refrence(parent_name, workshop_code):
#     random_num = random.randint(100000,999999)  # creates a random 6 digit number
#     first_three_par = parent_name[:3].upper()   #Capitalise first three letters of a parents name
#     workshop_code = workshop_code.upper()   #Turns the workshop code to upper case
#     booking_refrence = f"{first_three_par}{workshop_code}{random_num}"    #Joins it all back as a string
#     return booking_refrence  #Returns the string
# # print(create_booking_refrence("siti","pyt"))




# def valid_workshop_code(workshop_code):
#     valid = ["ROB", "WEB", "PYT" ] # valid workshop codes

#     if len(workshop_code) != 3: # checking valid length
#         print("Workshop code must contain exactly three characters")
#         return False
#     elif workshop_code.upper() not in valid:  
#         print("workshop code must be ROB, WEB or PYT")
#         return False
#     else:
#         # if code comes here, means its valid.
#         return True
# def calculate_booking_fee(workshop_code, number_of_students):
#     workshop_code = workshop_code.upper() # allow for  code to not be case sensitive
#     total = 0 # total cost
#     pricing = 0  # cost of each different workshop code
#     if workshop_code == "ROB":
#         pricing = 48
#     elif workshop_code == "WEB":
#         pricing = 36
#     else:
#         pricing = 42
#     total = pricing * number_of_students   #calculate the total for all students
#     if number_of_students >=3:
#         total = total * 0.9   # discount if theres 3 or more students
#     return total  #returns the total

# def create_booking_refrence(parent_name, workshop_code):
#     random_num = random.randint(100000,999999)  # creates a random 6 digit number
#     first_three_par = parent_name[:3].upper()   #Capitalise first three letters of a parents name
#     workshop_code = workshop_code.upper()   #Turns the workshop code to upper case
#     booking_refrence = f"{first_three_par}{workshop_code}{random_num}"    #Joins it all back as a string
#     return booking_refrence  #Returns the string
# # print(create_booking_refrence("siti","pyt"))















############################################################
# Task 5.4 [11]
############################################################

# Copy and paste your program from sub-task 5.3.

# The school requires an interface for the workshop booking system.

# the program must:
# Part 1: 
# - ask for the parent's name;
# - ask for a workshop code; call valid_workshop_code() to check the workshop code;
#       - keep asking until a valid workshop code is entered; store the valid workshop code in uppercase;
# - ask for the number of students;
#       - Validate that the input is a valid number
#       - keep asking until a whole number from 1 to 5 inclusive is entered;
# - call calculate_booking_fee() to calculate the booking fee;
# - call create_booking_reference() to create a booking reference;
# - display the booking reference and booking fee clearly.
# - Save the booking reference into a list called booking_list.
# - After each booking, ask the user to enter C to continue or Q to stop.

# Part 2:
# - save all the booking references in booking_list to the file workshop_bookings.txt, with one booking reference on each line;
# - store the total fee for all bookings to two decimal places at the end of the workshop_bookings.txt file.
#   e.g. "Total Fee : $192.86"

# Suitable input and output messages must be used.
# Save your JupyterLab notebook for Task 5.

# Task 5.4 
#______________________________________________________________
import random #Allows for random numbers
def create_booking_refrence(parent_name, workshop_code):
    random_num = random.randint(100000,999999)  # creates a random 6 digit number
    first_three_par = parent_name[:3].upper()   #Capitalise first three letters of a parents name
    workshop_code = workshop_code.upper()   #Turns the workshop code to upper case
    booking_refrence = f"{first_three_par}{workshop_code}{random_num}"    #Joins it all back as a string
    return booking_refrence  #Returns the string
# print(create_booking_refrence("siti","pyt"))




def valid_workshop_code(workshop_code):
    valid = ["ROB", "WEB", "PYT" ] # valid workshop codes

    if len(workshop_code) != 3: # checking valid length
        print("Workshop code must contain exactly three characters")
        return False
    elif workshop_code.upper() not in valid:  
        print("workshop code must be ROB, WEB or PYT")
        return False
    else:
        # if code comes here, means its valid.
        return True
def calculate_booking_fee(workshop_code, number_of_students):
    workshop_code = workshop_code.upper() # allow for  code to not be case sensitive
    total = 0 # total cost
    pricing = 0  # cost of each different workshop code
    if workshop_code == "ROB":
        pricing = 48
    elif workshop_code == "WEB":
        pricing = 36
    else:
        pricing = 42
    total = pricing * number_of_students   #calculate the total for all students
    if number_of_students >=3:
        total = total * 0.9   # discount if theres 3 or more students
    return total  #returns the total

def create_booking_refrence(parent_name, workshop_code):
    random_num = random.randint(100000,999999)  # creates a random 6 digit number
    first_three_par = parent_name[:3].upper()   #Capitalise first three letters of a parents name
    workshop_code = workshop_code.upper()   #Turns the workshop code to upper case
    booking_refrence = f"{first_three_par}{workshop_code}{random_num}"    #Joins it all back as a string
    return booking_refrence  #Returns the string
# print(create_booking_refrence("siti","pyt"))
booking_list = []  #Create the booking list
sum_total = 0  #Store the total cost of all bookings
while True:   #Loop back continuously for inputing of bookings
    par_name = input("What is the name of the parent?: ")
    while True:  #Validates for the proper workshop code
        ws_code = input("What is the workshop code?: ").upper()
        if valid_workshop_code(ws_code):  # Calls back previously defined function to return True if code is valid
            break
        else:
            print("Please enter a valid workshop code")
            continue

    while True:  #While loop to validate the correct number of students is inputed
        no_of_students = input("Please enter the number of students for this workshop")
        if not no_of_students.isdigit(): #Checks if input is a digit
            print("Please enter a positive integer")
            continue
        elif int(no_of_students) < 1 or int(no_of_students) >5:  #Validates the correct range of student is entered
            print("Please enter a whole number from 1 to 5 inclusive")
            continue
        else:
            no_of_students = int(no_of_students)  #Converts to integer for future use
            break
    total_cost = calculate_booking_fee(ws_code, no_of_students)  #Calculates total cost using previously created function
    booking_ref = create_booking_refrence(par_name,ws_code)  #Creates a booking refrence using previously created function
    print(f"Your booking fee is ${total_cost} and your booking ref is {booking_ref}")
    booking_list.append(booking_ref)   #Enters the booking list to the file to store
    continuation = input("Enter (C) to continue and enter (Q) to stop: ").upper()
    sum_total += total_cost  #Adds cost to the global variable
    if continuation == "Q":  #Breaks loop if needed
        break
    else:
        continue

with open("workshop_bookings.txt", "w") as file:  #Creates a text file 
    for booking in booking_list:  #Writes down every booking refrence in the list
        inputed_booking = f"{booking}\n"
        file.write(inputed_booking)
    file.write(f"Total fee : ${round(sum_total,2)}")   #Adds a line at the end for the total cost
    # file.write(f"Total fee : ${sum_total :.2f}")   #Adds a line at the end for the total cost