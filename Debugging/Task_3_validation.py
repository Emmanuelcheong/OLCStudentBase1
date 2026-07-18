#Backup
# while True:
# date = input("Enter the date (DD-MM-YYYY): ")
#     test = date
#     if len(test)= 10 and test[2]=="-" and test[5]=="-":
#         day = int(test[0:2])
#         month = int(test[3:])
#         year = int(test[6:])
#         check_year = year>1900 and year<=2000
#         check_month = month>=1 or month<=12
#         check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
#         check_day_30 = day<=31 and (month in [4,6,9,11])
#         check_day_Feb = month == 0 and ((day<=29 and year%4==0) or day<=28)
#         if check year:
#             if check_month:
#                 if check_day_31 or check_day_30 or check_day_Feb
#                     break
#                 else:
#                     print("Error in day")
#             else:
#                 print("Error in year")
#         else:
#             print("Error in month")
#     else:
#         print(Error in format")
# print("Date accepted")


while True:
    date = input("Enter the date (DD-MM-YYYY): ") #Indentation Error, line indented
    test = date
    if len(test) == 10 and test[2]=="-" and test[5]=="-": #Syntax Error, added an "="
        day = int(test[0:2])
        month = int(test[3:5]) #Logic error, didnt take the month correctly
        year = int(test[6:])
        check_year = year>=1900 and year<=2026  #Logic error, maximum year too short and minimum year not inclusive
        print(check_year)
        check_month = month>=1 and month<=12  #Logic error, used an "and" instead of an "or"
        print(check_month)
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        print(check_day_31)
        check_day_30 = day<=30 and (month in [4,6,9,11])  #Logic error, day should be 30
        check_day_Feb = month == 2 and ((day<=29 and year%4==0) or day<=28) #Logic error, month should be 2
        if check_year:  #Syntax Error, cshould be check_year
            if check_month:
                if check_day_31 or check_day_30 or check_day_Feb: #Syntax Error, added the missing ":"
                    break
                else:
                    print("Error in day")
            else:
                print("Error in month")  #Logic error, should be month error
        else:
            print("Error in year")  #Logic error, should be year error
    else:
        print("Error in format")  #Syntax Error, added the missing '"'
print("Date accepted")