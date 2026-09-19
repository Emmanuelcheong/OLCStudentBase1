
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[:3] + lastname
print("Your username is " + username)
while True:
    password = input("Please enter a password: ")
    if len(password) >= 8:
        print(f"Your user name is {password}")
        break
    else:
        print("Your password must be 8 characters or more")
        continue
while True:
    pass_check = input("Please reenter your password: ")
    if pass_check == password:
        print("Your password has been set.")
        break
    else:
        print("Password entries do not match. Please repeat the second entry of your password: ")
        continue