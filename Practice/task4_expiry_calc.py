# Task 5.1
def calculate_days(date):
    dd = int(date[:2])
    mm = int(date[3:])
    total_days = dd + (mm-1)* 30  #Calculate the number of days elapsed since the start of the year
    return total_days   #Returning the number of days calculated from the function

def days_difference(today_date,expiry_date):
    today = calculate_days(today_date)       #Calls upon the previous function to calculate the number of days elapsed since the start of the year
    expiry = calculate_days(expiry_date)
    days_left = expiry - today   #Calculates the number of days remaining until the expiry date 
    return days_left

def validate_date(date_str):
    validation = True
    dd_str = date_str[:2]     #Keeps the day section as string to not remove the 0 in front if there is one
    mm_str = date_str[3:]     
    if len(dd_str) != 2 or len(mm_str) != 2:     #Checks if the day and month are both 2 characters long
        print("Both the day (DD) and month (MM) must be two characters long")
        validation = False
    elif int(dd_str) < 1 or int(dd_str) > 30:       #Checks if date is a valid number
        print("The day (DD) must be between 1 and 30")
        validation = False
    elif int(mm_str) < 1 or int(mm_str) > 12:       #Checks if month is valid
        print("The month (MM) must be between 1 and 12")
        validation = False
    elif date_str[2] != "-":         #Checks for the existence of the dash
        print("Input must contain a dash (-) seperator between day and month")
        validation = False
    else:
        validation = True
    if validation == True:
        return True
    else:
        return False

# print(validate_date("4-12"))
# print(validate_date("01:01"))
# print(validate_date("012-01"))
# print(validate_date("01-033"))
# print(validate_date("55-08"))
# print(validate_date("01-55"))
# print(validate_date("01-02"))


    # return validation
while True:
    todays_date = input("What is todays date?: ")

    if validate_date(todays_date) == False:   #Calls upon validate_date() to check if the date entered is valid
        continue
    else:
        break

    # if validate_date(todays_date):
    #     break
    
while True:
    expiry_date = input("What is the expiry date?: ")
    if validate_date(expiry_date):      #Calls upon the validate_date() function to check if the date entered is valid   
        break

time_until_expiry = days_difference(todays_date, expiry_date)      #Calls upon the days_difference() function to calculate the amount of days between the 2 dates
if time_until_expiry > 0:    #Condition if food hasnt expired
    print(f"Item is fresh and will expire in {time_until_expiry} days")
elif time_until_expiry < 0:     #Condition if food has expired
    expired_days = abs(time_until_expiry)      #Removes the minus sign
    print(f"Item has expired {expired_days} days ago")
else:         #Condition if  food expires today
    print("Item will expire today")
# test = "31"
# test = int(test)
# if test < 1 or test > 30:
#     print("doesnt work")
# else:
#     print("works")
