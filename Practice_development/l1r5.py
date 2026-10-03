def getgradepoint(mark):   #Defining function
    if mark >= 75:   #Loops through and returns the gradepoint
        return 1
    elif mark >= 70:
        return 2
    elif mark >=65:
        return 3
    elif mark >=60:
        return 4
    elif mark >= 55:
        return 5
    elif mark >=50:
        return 6
    elif mark >= 45:
        return 7
    elif mark >= 40:
        return 8
    else:
        return 9

def calL1r5(result):   #Defining function
    total = 0
    hcl_score = 0
    el_score = 0
    for subject,score in result.items():   #Looks through key and value in the dictionary
        if subject == "English":   #Checks if subject is a language
            el_score = getgradepoint(score)
        elif subject == "Higher Chinese":
            hcl_score = getgradepoint(score)
        else:
            total += getgradepoint(score)   #If not a language, add the gradepoint to the l1r5
    if hcl_score > el_score:   #Checks which language score is higher and adds the better grade point to the total
        total += getgradepoint(hcl_score)
    else:
        total += getgradepoint(el_score)
    return total    #returns the l1r5 as output

subjects = {"English":0, "Higher Chinese":0, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0}
for subject in subjects:
    while True:
        user_score = input(f"What is the score for {subject}?: ")
        if not user_score.isdigit():
            print("Score must be a number")
        elif user_score>100 or user_score<0:
            print("Score must be a number from 0 to 100 inclusive")
        else:
            subjects[subject] = user_score
l1r5 = calL1r5(subjects)

with open("resultslip.txt","w") as file:
    for subject,score in subjects.items():
        file.write(f"{subject}   {score}  ({getgradepoint})")