
##############################################################
### ASCII ord() and chr() for password generation
##############################################################

# #Generate a Simple Password
# # Write a Python program that generates a random password of a given length 
#     using ASCII printable characters.
# # Example input: length = 8
# # Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# # HINT: ASCII printable characters range from 33 to 126

# Sample solution 

# import random

# length = 8
# password = ""
# for i in range(length):
#     char = chr(random.randint(33, 126))  
#     password += char
# print(f"Generated password: {password}")


###########################################################
# Generate a Password with Specific Character Types
# Scenario 1: Corporate Password Policy - Basic Compliance
# One of your clients, a fintech company, has implemented a basic password policy. 
# All system-generated passwords must:
# - Be of a specific length
# - Include at least 1 uppercase letter, 1 lowercase letter, and 1 digit

# Your task: Write a Python program to generate such a password.
# Example: input = 8 → output = 'aB3xG2#1'

# HINT: Use ASCII:
# - Uppercase letters: 65-90
# - Lowercase letters: 97-122
# - Digits: 48-57


# Write and test your code here
import random
# password = chr(random.randint(97,122)) + chr(random.randint(65,90)) + chr(random.randint(48,57)) 
# length = int(input("How long do you want the password to be: "))
# for i in range(length-3):
#     char = chr(random.randint(33,126))
#     password += char
# print(password)


###########################################################
# Exclude Specific Characters in Password
#  Scenario 2: Readability-Enhanced Password Generator
# A logistics firm found that users often confuse similar-looking characters 
# (like 'l', '1', 'I', 'O', and '0') when reading out passwords over the phone.

# To improve usability, you're tasked to generate passwords that:
# - Are of a specific length
# - Exclude these confusing characters: 'l', '1', 'I', 'O', '0'

# Example: input = 8, exclude = 'l1IO0' → output = 'aB3xG#2!'
# Hint: Any character in 33-126 except ASCII codes 48, 49, 73, 79, 108


# Write and test your code here
# password = ""
# confusing_char = "l1IO0"
# length = int(input("How long do you want the password to be: "))
# for i in range(length):
#     while True:
#         char = chr(random.randint(33,126))
#         if char in confusing_char:
#             continue
#         else:
#             break
#     password += char
# print(password)


###########################################################
# Password with Special Characters
# Scenario 3: System Admin Access Passwords
# System administrators require strong passwords with at least 2 special characters 
# to prevent brute-force attacks.

# Your task:
# - Generate a password of a given length
# - Ensure it includes at least two special characters
#   (characters that are neither letters nor digits, e.g., '@', '#', '$', '%', etc.)

# Example: input = 8 → output = 'aB3@xG#2'
# Hint: ASCII 33-47: ! " # $ % & ' ( ) * + , - . /

# Write and test your code here
# length = int(input("How long do you want your password to be: "))
# while True:
#     check = 0
#     password = ""
#     for i in range(length):
#         char = chr(random.randint(33,126))
#         if ord(char) >= 33 and ord(char) <= 47:
#             check += 1
#         password += char
#     if check < 2:
#         continue
#     else:
#         break
# print(password)
        





###########################################################
# Scenario 4: High-Security Access Control
# A secure military application demands passwords that follow strict composition rules
# The password must contain:
# - At least 2 uppercase letters
# - At least 2 lowercase letters
# - At least 2 digits
# - At least 2 special characters

# Write a Python program that:
# - Accepts the desired password length
# - Ensures the final password follows these rules exactly

# Example: input = 8 → output = 'A1b#C2d!'
# Hint: 
# Uppercase letters: 65-90
# Lowercase letters: 97-122
# Digits: 48-57
# Special characters (non-alphanumeric)
# 33-47, 58-64, 91-96, 123-126


# Write and test your code here








###########################################################
# Calculate Checksums for a List of Network Messages
#
# A computer needs to send several text messages across a network.
# Before each message is sent, the computer calculates a checksum.
#
# The checksum is calculated using this algorithm:
# 1. Convert each character in the message into its ASCII value.
# 2. Add up all the ASCII values.
# 3. Calculate the total modulo 256.
#
# Checksum = total ASCII value % 256
#
# Your task:
# Write a Python program that:
# - Uses the given list of 5 messages
# - Loops through each message in the list
# - Calculates the checksum of each message
# - Outputs each message and its checksum
#
# Expected output:
#
# The server is ready -> 9
# Send the file now -> 31
# Login request accepted -> 123
# Data packet received -> 121
# Connection closed -> 170
#
# HINT:
# - Spaces are also characters and must be included in the checksum.
# - Use ord(character) to get the ASCII value of a character.
# - Use % 256 to calculate the checksum.
#
# Write and test your code here

# messages = [
#     "The server is ready",
#     "Send the file now",
#     "Login request accepted",
#     "Data packet received",
#     "Connection closed"
# ]
# for message in messages:
#     total = 0
#     for char in message:
#         total += ord(char)
#     check_sum = total % 256
#     print(f"{message} -> {check_sum}")