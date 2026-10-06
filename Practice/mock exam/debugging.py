
valid = 0
invalid = 0  #1) Logic error, invalid count should start from 0

print("Welcome to the Email Validator!")
print("Type 'exit' to quit the program.\n")

while True:   #2) Syntax error, missing a ":"
    email = input("Enter an email address: ").strip()

    if email.lower() == "exit":    #7) Syntax error, forgot the "()"
        break   #6) Logic error, should break out of loop if input is "exit"

    if len(email) < 10:    #8) Logic error, should be invalid if less than 10 characters
        print("Email is too short.\n")
        invalid += 1
        continue

    at_index = email.find("@")    #3) Syntax error, used a "==" instead of a "="

    if at_index == -1 or email.find("@", at_index + 1) != -1:
        print("Email must contain exactly one '@' symbol.\n")
        invalid += 1
        continue

    if at_index == 0 or at_index == len(email) - 1:   #9) Syntax error, used a "." instead of a "()"
        print("'@' cannot be at the start or end of the email.\n")
        invalid += 1
        continue

    dot_index = email.find(".", at_index + 1)

    if dot_index == -1 or dot_index == at_index + 1:
        print("There must be a '.' after the '@' symbol, and not immediately after it.\n")
        invalid += 1  #4) Syntax error, should add by 1 and not "one"
        continue

    print("Valid Email!\n")
    valid += 1   #10) Logic error, should be changing valid and not invalid


print("\nTotal valid emails entered: ", valid)   #5) Syntax error, did not close the bracket
print("Total invalid emails entered: ", invalid)