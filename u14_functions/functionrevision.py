###########################################################
# Part 2. IN-CLASS Practice Exercises
# Topic: Creating Functions and Calling Functions


# =========================================================
# A. FUNCTIONS THAT PRINT RESULTS DIRECTLY
# (The function itself prints the output.)
# =========================================================

#------------------------------------------------------------
# Exercise 1: Student Name Tag
# During orientation, each student receives a printed name tag.
#
# Write a function print_name_tag(name, class_name) that prints:
# Welcome 
# Class: 
#
# Example function call:
# print_name_tag("Alicia", "3E1")
#
# Sample output:
# Welcome Alicia
# Class: 3E1
# def print_name_tag(name, class_name):
#     print(f"Welcome {name}")
#     print(f"Class: {class_name}")
# print_name_tag("Alicia", "3E1")

#------------------------------------------------------------
# Exercise 2: Hotel Booking Charge
# A hotel charges $120 per night for a room.
#
# Write a function booking_confirmation(guest_name, nights) that
# calculates the total cost and prints:
# Booking confirmed for 
# Number of nights: 
# Total cost: $
#
# Example function call:
# booking_confirmation("Mr Lee", 3)
#
# Sample output:
# Booking confirmed for Mr Lee
# Number of nights: 3
# Total cost: $360
# def booking_confirmation(guest_name, nights):
#     room_cost = nights*120
#     print(f"Booking confirmed for {guest_name}")
#     print(f"Number of nights {nights}")
#     print(f"Total cost: ${room_cost}")
# booking_confirmation("Mr Lee", 3)


#------------------------------------------------------------
# Exercise 3: Weather Advisory
# A weather station wants to display a weather advisory for a city.
#
# Write a function weather_report(city, temperature) that prints:
# City: 
# Temperature: °C
# Advisory: 
#
# The advisory should be:
# "Hot" if temperature is 32 or above
# "Warm" if temperature is from 25 to 31
# "Cool" if temperature is below 25
#
# Example function call:
# weather_report("Singapore", 31)
#
# Sample output:
# City: Singapore
# Temperature: 31°C
# Advisory: Warm
# def weather_report(city, temperature):
#     advisory = ""
#     print(f"City: {city}")
#     print(f"Temperatire: {temperature}°C")
#     if temperature >= 32:
#         advisory = "Hot"
#     elif temperature >= 25 and temperature <= 31:
#         advisory = "Warm"
#     else:
#         advisory = "Cool"
#     print(f"Advisory: {advisory}")
# weather_report("Singapore", 31)
# =========================================================
# B. FUNCTIONS THAT RETURN A VALUE
# (The function returns the answer. Print it outside.)
# =========================================================

#------------------------------------------------------------
# Exercise 4: Canteen Meal Cost
# A school canteen sells rice bowls for a fixed price each.
#
# Write a function meal_cost(price, quantity) that returns
# the total cost.
#
# Then call the function and print the returned value.
#
# Example function call:
# total = meal_cost(3.5, 2)
# print("Total Cost: $", total)
#
# Sample output:
# Total Cost: $ 7.0



#------------------------------------------------------------
# Exercise 5: Library Book Status
# Assume it is the month of April, which has 30 days.
#
# Write a function book_status(today, due_date) that returns:
# "Overdue" if today is later than the due date
# "Due today" if today is the same as the due date
# "Not due" if today is earlier than the due date
#
# Then call the function and print the returned value.
#
# Example function call:
# status = book_status(14, 15)
# print("Status:", status)
#
# Sample output:
# Status: Not due



#------------------------------------------------------------
# Exercise 6: Test Grade
# A teacher wants to assign a grade based on a student's mark.
#
# Write a function get_grade(mark) that returns:
# "A" if mark is 75 or above
# "B" if mark is from 60 to 74
# "C" if mark is from 50 to 59
# "D" if mark is below 50
#
# Then call the function and print the returned grade.
#
# Example function call:
# grade = get_grade(68)
# print("Grade:", grade)
#
# Sample output:
# Grade: B



#------------------------------------------------------------
# Exercise 7: Taxi Fare
# A taxi company charges:
# - a basic fare of $3.20
# - plus $0.55 for every 1 km travelled
#
# You may assume the distance can include halves, such as 4.5 km.
# This means:
# - 1 km costs $0.55
# - 0.5 km costs $0.275
#
# Write a function calculate_taxi_fare(distance) that returns
# the total fare.
#
# Then call the function and print the returned value.
#
# Example function call:
# fare = calculate_taxi_fare(4.5)
# print("Fare: $", round(fare, 3))
#
# Sample output:
# Fare: $ 5.675



#------------------------------------------------------------
# Exercise 8: Data Remaining
# A user wants to check how much mobile data is left in the plan.
#
# Write a function data_left(plan_gb, used_gb) that returns
# the amount of data left.
#
# If used_gb is more than plan_gb, return 0.
#
# Then call the function and print the returned value.
#
# Example function call:
# remaining = data_left(20, 13.5)
# print("Data Left:", remaining, "GB")
#
# Sample output:
# Data Left: 6.5 GB



# =========================================================
# C. FUNCTIONS THAT CALL ANOTHER FUNCTION
# (Extension questions on modular programming.)
# =========================================================

#------------------------------------------------------------
# Exercise 9: Concert Ticket Booking
# A school concert sells:
# - student tickets at $6 each
# - adult tickets at $12 each
#
# Write a function get_ticket_price(ticket_type, quantity)
# that returns the total ticket price.
#
# Then write a function booking_summary(name, ticket_type, quantity)
# that calls get_ticket_price() and prints:
# Name: 
# Ticket Type: 
# Quantity: 
# Total Price: $
#
# Example function call:
# booking_summary("Rina", "student", 4)
#
# Sample output:
# Name: Rina
# Ticket Type: student
# Quantity: 4
# Total Price: $24



#------------------------------------------------------------
# Exercise 10: Online Shop Bill
# An online shop gives free delivery if the order total is $50 or more.
# Otherwise, delivery costs $4.
#
# Write a function delivery_charge(order_total) that returns
# the delivery charge.
#
# Then write a function final_bill(customer_name, order_total)
# that calls delivery_charge() and prints:
# Customer: 
# Order Total: $
# Delivery Charge: $
# Final Amount: $
#
# Example function call:
# final_bill("Nora", 35.5)
#
# Sample output:
# Customer: Nora
# Order Total: $35.5
# Delivery Charge: $4
# Final Amount: $39.5


##############################################################
##### MOCK QUESTION ##########################################
##############################################################
# The task is to write a program that checks whether a food item has expired based on 
# its expiry date and today’s date. Dates are entered in the format "DD-MM".

# All code should have appropriate comments and meaningful identifiers. [2]
# 
# ________________________________________
# Task 5.1 [4]
# Write a calculate_days( ) function that accepts a date parameter in the format "DD-MM".
# The function must calculate and return the total number of days elapsed since 01-01, 
# assuming 30 days per month
# ________________________________________
def calculate_days(date):
    day_section = int(date[:2])
    month_section = int(date[3:])
    sum_days = (day_section-1) + ((month_section - 1)*30)
    return sum_days




# Test your code using the values below
# print(calculate_days("01-02"))
# print(calculate_days("30-01"))
# print(calculate_days("30-02"))
# print(calculate_days("30-12"))


# ________________________________________
# Task 5.2  [3]
# Write a days_difference( ) function that takes two parameters:
# •	today (format "DD-MM")
# •	expiry (format "DD-MM")

# The function will check if an item has expired and return the number of days 
# between today’s date and the expiry date.
# •	Expiry is calculated by subtracting the today’s date from the expiry date. 
# You must use the calculate_days() function to retrieve the number of days between 
# today’s date and expiry date. Note that the number of days could be negative.
# You can assume both dates are always within the same year.
# 
# ________________________________________

def days_difference(today,expiry):
    day_diff = calculate_days(expiry) - calculate_days(today)
    return day_diff


# ________________________________________
# Task 5.3 [8]
# Write a validate_date( ) function that accepts one parameter:
# •	date_str (a string in the format "DD-MM")
# The function must check whether the input date is valid according to the following rules:
# 1.	The input must contain a dash (-) separator between day and month.
# 2.	Both the day (DD) and month (MM) must be two characters long (e.g. "05-04" not "5-4").
# 3.	The day (DD) must be between 1 and 30 (inclusive).
# 4.	The month (MM) must be between 1 and 12 (inclusive).
# If all conditions are met, the function should return True.
# If any condition fails, the function should return False.
# Displays appropriate messages for invalid input. You may assume the input is always a string.
# ________________________________________

def validate_date(date_str):
    pos = date_str.find("-")
    day_sect = date_str[:int(pos)]
    month_sect = date_str[int(pos)+1:]
    if pos == -1:
        print("The input must contain a dash (-) separator between day and month.")
        return False
    elif not(day_sect.isdigit() and month_sect.isdigit()):
        print("Date and Month must be a number")
        return False
    elif len(day_sect) != 2 or len(month_sect) != 2:
        print("Both the day (DD) and month (MM) must be two characters long")
        return False
    elif int(day_sect) < 1 or int(day_sect) > 30:
        print("The day (DD) must be between 1 and 30 (inclusive).")
        return False
    elif int(month_sect) < 1 or int(month_sect) > 12:
        print("The month (MM) must be between 1 and 12 (inclusive).")
        return False
    else:
        return True



# print(validate_date("01#01"))
# print(validate_date("aa-01"))
# print(validate_date("01-aa"))
# print(validate_date("50-01"))
# print(validate_date("05-50"))
# print(validate_date("0310"))
# print(validate_date("03-10"))

# ________________________________________
# Task 5.4 [6]
# Create a simple text-based user interface that:
# •	Prompts and validates today’s date in "DD-MM" format.
# o	You must use the validate_date() function to validate today’s date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Prompts and validates the expiry date in "DD-MM" format.
# o	You must use the validate_date() function to validate the expiry date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Compute if the item has expired. You must use the days_difference() function. 
#     If the number of days is positive, the item has not expired. 
#          Output “Item is fresh and will expire in  days.”
#     If the number of days is negative, the item has expired. 
#          Output “Item has expired  days ago.”
#     If the number of days is 0, then the item expires today. 
        #    Output “Item will expire today!”
# ________________________________________
while True:
    todays_date = input("Please enter todays date: ")
    if not(validate_date(todays_date)):
        continue
    else:
        break
while True:
    expiry_date = input("Please enter the expiry date: ")
    if not(validate_date(expiry_date)):
        continue
    else:
        break
day_diff = days_difference(todays_date,expiry_date)
if day_diff > 0:
    print(f"Item is fresh and will expire in {day_diff} days.")
elif day_diff <0:
    print(f"Item has expired {abs(day_diff)} days ago.")
else:
    print("Item will expire today!")
