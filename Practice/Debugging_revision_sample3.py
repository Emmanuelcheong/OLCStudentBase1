name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #2) Count should start from zero

flag = True
while flag == True:     #3) Logic error  check if True to start the loop
    name = input("Enter student's name: ")       #1) Syntax Error, String uses the same '
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100:   #5) should be and instead of or 
            break
        else:
            print('Invalid mark!')
    mark_list += [mark]    #4) Logic error  Remove indent to add score once validated
    count += 1
    if mark >= 75:    #6) Should be >= instead of just >
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]   #7) should be [name] instead of (name)
    more = str(input('Would you like to enter another score, Y or N?: '))    #8) more should be in str and not int
    if more == 'N':
        flag = False

average = round(sum(mark_list)/len(mark_list), 2)    #9) should be sum and not max
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")    #10) count should be in a string and not a integer
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))

# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))