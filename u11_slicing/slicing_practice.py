# String and List Operators
# Using + to Concatenate
# List Slicing

'''
Question 1: Extract a portion of a list and creates a new list
that contains only the first three elements of the original list.
Example Input: [1, 2, 3, 4, 5]
Example Output: [1, 2, 3]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[:3] # from start, up to 3 but not including 3
# print(newlist) # returns [1,2,3]

'''
Question 2: Get the last three items of a list.
Ask the user for a list of numbers and print the last three items.
Example Input: [10, 20, 30, 40, 50]
Example Output: [30, 40, 50]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[-3:] # from last 3rd, to the end
# print(newlist) # returns [3,4,5]

'''
Question 3: Create a sub-list from a list using slicing.
Given a list of elements, write a function that returns a
sublist from the second element to the second last element.
Example Input: [0, 1, 2, 3, 4, 5]
Example Output: [1, 2, 3, 4]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[1:-1] # from the second element to the second last element
# print(newlist) # returns [2,3,4]

'''
Question 4: Reverse a list using slicing.
Write a function that takes a list and returns it reversed.
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[::-1] # reverse it
# print(newlist) # returns [5,4,3,2,1]

'''
Question 5: Slice a list into halves.
Divide a list into two equal halves and returns both halves.
You may assume that the list has an even number of items
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 2, 3]  [4, 5, 6]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# listlen = len(inlist) # find length of list
# midindex = listlen // 2 # find the middle index / position
# first_half = inlist[:midindex]
# second_half = inlist[midindex:]
# print(first_half) # returns [1, 2, 3]
# print(second_half) # returns [4, 5, 6]

'''
Question 6: Extract every second element from a list.
Write a function that returns a list of every second element from the given list.
Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
Example Output: ['b', 'd', 'f']
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# newlist = inlist[1::2] # start from 1 (2nd place, to end, increments of 2)
# print(newlist) # returns [2,4,6]

'''
Question 7: Remove the first and last elements of a list using slicing.
Create a function that takes a list and returns it without
the first and last elements.
Example Input: [0, 1, 2, 3, 4]
Example Output: [1, 2, 3]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# newlist = inlist[1:-1]
# print(newlist) # returns [2, 3, 4, 5]

'''
Question 8: Create code to reverse the order of elements in a
list only from the second to the last but one.
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 5, 4, 3, 2, 6]
'''
## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# second_to_last = inlist[1:-1] # get 2nd to last
# reversed_middle = second_to_last[::-1] # reverse 2nd to last
# liststart = [inlist[0]] # retrieves 1st char and converts to list
# listend = [inlist[-1]] # retrieve last char and convert to list
# newlist = liststart + reversed_middle + listend
# print(newlist) # returns [1, 5, 4, 3, 2, 6]


'''
# Question 9: Extract the first three characters from a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here
# input_str = (input("Enter a string: "))
# print(input_str[:3])

'''
# Question 10: Extract the last three characters from a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here
# input_str = input("Enter a string: ")
# slice_index = len(input_str) - 3
# print(input_str[slice_index:])
'''
# Question 11: Extract a subset of a list from index 2 to 5
# Test case 1: example input: 1 2 3 4 5 6 7, 
example output: [3, 4, 5, 6]
# Test case 2: example input: 10 20 30 40 50 60, 
example output: [30, 40, 50, 60]
'''
## Write and test your code here
# input_list = input("Enter a list of numbers")
# list_input = input_list.split(" ") 
# print(list_input[2:6])
'''
# Question 12: Extract every second character from a string
# Test case 1: example input: hello, example output: hlo
# Test case 2: example input: Python, example output: Pto
'''
## Write and test your code here
# input_str = input("Enter a string: ")
# print(input_str[::2])

'''
# Question 13: 
# Write a function called mid3(instring)
# Extract the middle three characters from a string
# Check that the incoming string must be an odd length, 
# Test case 1: example input: abcdefg, example output: cde
# Test case 2: example input: helloworld, example output: Invalid, Even length
'''
## Write and test your code here

# def mid3(instring):
#     if len(instring) % 2 == 0:
#         return print("Invalid, Even length")
#     else:
#         mid_pos = len(instring) / 2
#         first_pos = mid_pos -1
#         last_post = mid_pos + 2
#         return print(instring[int(first_pos):int(last_post)])
# string = input("Enter a string: ")
# mid3(string)
'''
# Question 14: Extract the first half of a string (assume its even number of characters)
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here
# input_str = input("Enter a string: ")
# half_pos = len(input_str) // 2
# print(input_str[:int(half_pos)])

'''
# Question 15: Extract the second half of a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here
# input_str = input("Enter a string: ")
# half_pos = len(input_str) // 2
# print(input_str[int(half_pos):])
'''
Question 16:
Write a function to split a string into half
and return the first half and second half
Your function must handle an even/ odd number length of characters
# If the length is odd, you will ignore the middle character
Example Input: "SINGING" Example Output: SIN, ING
Example Input: "FLYING" Example Output: FLY, ING
'''
## Write and test your code here
# input_str = input("Enter a string: ")
# if len(input_str) % 2 == 1:
#     first_half = (len(input_str) / 2) - 0.5
#     second_half = first_half + 1
#     print(input_str[:int(first_half)])
#     print(input_str[int(second_half):])
# else:
#     half_str = len(input_str) / 2
#     print(input_str[:int(half_str)])
#     print(input_str[int(half_str):])
'''
# Challenge 1:
Write a function `validate_nric(nric: str) returns a bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''
## Write and test your code here
# def validate_nric(nric):
#     if nric[:1] not in "STFG":
#         return False
#     elif not nric[1:8].isdigit():
#         return False
#     elif not nric[-1:].isupper(): 
#         return False
#     else:
#         return True
# print(validate_nric("A1234567D"))
    
    

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Error Test: Input: "John Doe", Output: False
Boundary Test: Input: "John", Output: False
'''
## Write and test your code here


    

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''
## Write and test your code here


    

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''
## Write and test your code here




'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''
## Write and test your code here



    

'''
Challenge 6:
A programmer is writing a program to calculate the 
check digit for a 12-digit integer.

The check digit is calculated by multiplying the digits 
in odd positions by 3 and the digits in even positions by 1. 
These values are added together to produce a total. 
The total is subtracted from the next multiple of 10 to 
give a final value. If the final value is 10, the check digit is X.

Example: 
12-digit integer = 1  0  3  4  5  6  2  7  1  0  1  3
Result           = 3  0  9  4  15 6  6  7  3  0  3  3
Total = 3 + 0 + 9 + 4 + 15 + 6 + 6 +7 + 3 + 0 + 3 + 3 = 59
The next multiple of 10 is 60 (*hint: nextnum = math.ceil(num/10) * 10)
So, check digit = 60 - 59 = 1

(a) The The program code function calculate() takes a 
12-digit number as a parameter. It calculates the 
check digit and returns the check digit.

Write the code for the function calculate [6]

(b) The main program:
•	Takes as input a 12-digit number until a valid 
12-digit integer is entered
•	Calls the function calculate() with the valid input 
as a parameter
•	Outputs the number with the check digit as its 13th digit

Write the code for the main program. [5]

Test that:
103456271013 = 1
123456789012 = 0
135792468013 = 5
'''
## Write and test your code here


    

'''
Challenge 7:
A developer needs to extract specific characters from a 
given string to generate a user ID.

(a) Write a function generate_user_id(name, birthdate) 
that takes a user's full name as a single string in the 
format "First Last" and a birthdate in the format "YYYYMMDD". 
The function should return a user ID consisting of:

- The first three letters of the last name (in uppercase),
- The last two digits of the year of birth,
- The first letter of the first name (in lowercase).
For example:
generate_user_id("John Doe", "19901225") should return DOE90j.
[6 marks]

(b) Write a main program that:

- Takes as input a full name and birthdate,
- Calls the generate_user_id() function,
- Outputs the generated user ID.
Test cases:

generate_user_id("Alice Tan", "20030515") should return TAN03a.
generate_user_id("Michael Johnson", "19850911") should return JOH85m.
[4 marks]
'''
## Write and test your code here


    

'''
Challenge: Credit Card Validation
A financial institution needs to verify the validity of credit card numbers 
using the Luhn algorithm.

Task 1: Implementing the Luhn Algorithm
(a) Write a function is_valid_credit_card(card_number) that takes 
a credit card number as a string and checks if it is valid according 
to the Luhn algorithm. The function should:

- Start from the rightmost digit (check digit) and move left.
- Double every second digit. If the doubling results in a number greater 
    than 9, subtract 9 from it.
- Sum all the digits (including those not doubled).

If the total sum is divisible by 10, return True 
(indicating the card number is valid); otherwise, return False.

Example:

is_valid_credit_card("4539148803436467") should return True.
is_valid_credit_card("1234567812345670") should return False.
[6 marks]

Task 2: Testing the Function
(b) Test your function with the following credit card numbers 
and determine if they are valid:

4539148803436467
1234567812345670
4485275742308327
6011514433546201
1234567812345678
Write the expected output for each test case.
'''
## Write and test your code here
