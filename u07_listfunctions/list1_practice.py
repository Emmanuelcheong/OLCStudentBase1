list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
#Find length without len()
count = 0
for num in list1:
    count+= 1
print(count)
#Find total without sum()
total = 0 
for num in list1:
    total += num
#Find average
avg = total/count
print(avg)
#Find max/min
biggest_num = list1[0]     #assume first in biggest/smallest
for num in list1:
    if num > biggest_num:
        biggest_num = num
print(biggest_num)

smallest_num = list1[0]
for num in list1:
    if num < smallest_num:
        smallest_num = num
print(smallest_num)







##############################################

shapes = ["star", "square", "circle", "triangle"]
colors = ["red","green","yellow","blue"]

# -----------------------------------------
# Task 1
# Write a code to loop through both list
# and match the color to the shape

# Example output
# red star
# green square
# yellow circle
# blue triangle
# shapes = ["star", "square", "circle", "triangle"]
# colors = ["red","green","yellow","blue"]
# for i in range(len(shapes)):
#     print(f"{colors[i]} {shapes[i]} ")
# -----------------------------------------
# Task 2
# ask the user to input a shape
# output the color for that shape


# Example output
# Enter a shape: circle
# The color for circle is yellow
# shapes = ["star", "square", "circle", "triangle"]
# colors = ["red","green","yellow","blue"]
# for i in range(len(shapes)):
#     print(f"{colors[i]} {shapes[i]} ")
# shape_inp = input("Please input a shape ")
# index = shapes.index(shape_inp)
# print(f"The color for {shape_inp} is {colors[index]}")
#If not allowed to use .index
# shapecheck = input("enter a shape:")
# if shapecheck in shapes:
#     for i in range(len(shapes)):
#         if shapecheck == shapes[i]:
#             print(f"The colour for {shapecheck} is {colors[i]}")
# else:
#     print(f"{shapecheck} does not exists")
#To check for index
#tocheck = "name of the stuff"
#for i in range(len(shapes)):
#   if tocheck == shapes[i]:
#       index = i



#Find the length of list without using len()

#Find the total of list of numbers without using sum()

# find the average ofa list

# find the max/min in a list without using their respective functions