
name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #10) Logic error, count should start form 1

flag = True
while flag == True:  #1) Runtime error, flag must be true
    name = input("Enter student's name: ")  #2) Syntax error, used repeat of '
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100:   #3)Logic error, condition should be and
            break
        else:
            print('Invalid mark!')
    mark_list += [mark]   #4)Logic error, should be dedented
    count += 1
    if mark >= 75:   #5)Logic error, not inclusive of 75
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]  #6)Logic error, should be [] instead of ()
    more = input('Would you like to enter another score, Y or N?: ') #7)Logic error, should be str and not int
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2)   #8)Logic error, should be sum() and not max()
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")   #9)Syntax Error, should be converted to string
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))