#------------------------------------------------------------
# Exercise 14: Combined Checks (Password Policy)
# Requirements:
# - Non-empty
# - Length between 8 and 16
# - Must contain at least one digit 0-9
# - No spaces
# Keep prompting until valid, then print "Password set".
# Sample Inputs: "abc" (invalid), "abcd efgh1" (invalid), "GoodPass1" (valid)
#------------------------------------------------------------

while True:
    password = input("Enter a password: ")
    hasdigit = False
    hasspace = False
    hasspecial = False
    #Check whether password has number and no space
    for c in password:
        if c.isdigit():
            hasdigit = True
        if c.isspace():
            hasspace = True
        if c in "!@#$%^&*":
            hasspecial = True
    if password == "":
        print("Password cannot be empty")
    if len(password) < 8 or len(password) > 16:
        print("Password must be between 8 and 16 characters")
    elif hasdigit == False:
        print("Password must contain a number from 0 to 9")
    elif hasspace:
        print("Password cannot contain spaces")
    else:
        print(f"Password {password} has been set")
        break
