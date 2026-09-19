def div_2(number):
    halved = int(number/2)
    return halved

def odd_or_even(number):   #defining function
    if number %2 == 0:     #Checks if number is even
        return "Even"     #Outputs respective message
    else:
         return "Odd" 

def prime(number):     #Defining function
    output = "Not prime"
    if odd_or_even(number) == "Even":    #Calls upon previous function to check if number is even
        return output
    if number == 1:   #Prime number cannot be 1
        return output
    half_num = div_2(number)   #Get half the number using previous function
    for i in range(number):     
        if i == 0:   #Ensures i is not 0 so theres no division by 0
            continue
        else:
            if i != 1 and i < half_num and number/i == int(number/i):   #Ensures number is not 1, and checks if dividing the number by any divisor up to half of it will give a whole number
                return output    #If it can be divided by a divisor up to half, or is 1, output as not a prime
    return "Prime"   #Else return as a prime number

while True:    #Loops until broken
    user_num = input("Please enter a whole number: ")     #Takes user input
    if user_num.isdigit():   #Checks if input is only a number
        break   #If so breaks out of loop
    else:    #If anything inside the input isnt a digit, cotninues the loop
        print("Your number must be a whole number")
        continue
if prime(int(user_num)) == "Prime":    #Calls upon previous function to check if validated input is a prime
    print("Your inputted number is a prime number")
else:   
    print("Your inputted number is not a prime number")