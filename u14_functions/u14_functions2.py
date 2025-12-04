#Task 5.1
def calculate_minutes(time):
    total=0
    hours = int(time[:2]) * 60 # calculate number of hours
    mins = int(time[3:])
    total = hours + mins # add up the hours and minutes
    return total

def calculate_wage(clock_intime, clock_outtime):
    time_worked = calculate_minutes(clock_outtime) - calculate_minutes(clock_intime)
    hours_payable = int(time_worked / 60)  # time_worked // 60 # floor divide
    total_wage = 0
    for i in range(hours_payable):
        if i < 8: 
            total_wage += 20 # loop through for normal hours to find normal wage
        else:
            total_wage += 30 # loop through for OT hours to find OT wage
    return total_wage

def validate(time):
    hh = int(time[:2]) # retrieve the hour portion from time
    mm = int(time[3:])
    if hh > 23 or hh < 0:
        print("hours must be between 00 and 23") # validate for proper hour
        return False
    elif mm > 59 or mm < 0:
        print("minutes must be between 00 and 59")
        return False
    elif time.find(":") == -1:
        print("must contain colon (:) seperator")
        return False
    else: 
        return True

while True:
    while True:
        intime = input("Enter clock-in time (HH:MM) : ")
        if validate(intime) == True:
            break
    while True:
        outtime = input("Enter clock-out time (HH:MM) : ")
        if validate(outtime) == True:
            break

    inminutes = calculate_minutes(intime)
    outminutes = calculate_minutes(outtime)

    if outminutes < inminutes:
        print("Ending time cannot be before starting time. Try again")
    else:
        wages = calculate_wage(intime, outtime)
        print(f"Your wage is ${wages}")
        break