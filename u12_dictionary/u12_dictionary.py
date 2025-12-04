#How to define dictionary
menu = {"pasta":"$2.00",
        "pizza": "$18.00",
        "fries": "$4.00"}
#Retrieve a value from the key
val1 = menu["pizza"]
print(val1)

#How to change a value of a key
menu["pasta"] = "$4.00"
print(menu)

#How to add a new key:value pair
menu["mercedes"] = "$500 000.00"
print(menu)
#Delete a key/value pair
del menu["mercedes"]
print(menu)

#How to check if key exists
if "pasta" in menu:
    print("I sell pasta")
else:
    print("I dont sell pasta")

#Loop through a dictionary (1)
for key in menu:
    print(key)
    #To print the value
    print(menu[key])
#Shortcut(2) Function
for key,value in menu.items():
    print(f"{key}: {value}")






########################################
########################################################
# Question 3:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
donations = {
    'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
    'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
    'Class 4E': 415, 'Class 5F': 390
}
# Answer for Question 3 here
min_class = ""
min_amt = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for classname, amount in donations.items():
    if amount < min_amt:
        min_amt = amount
        min_class = classname
print(f"{min_amt},{min_class}")













# dict1 = {"hamburger": 5, 
#          "pasta": 10, 
#          "fries": 2}

# # add / amend
# dict1["hamburger"] = 10

# # for key,value in dict1.items():
# #     print(key)
# #     print(value)

# # for key in dict1:
# #     print(key) # key
# #     print(dict1[key]) # value

# def oddoreven(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
