def getgradepoint(mark):
    gp = 0
    if mark >= 75:
        gp = 1
    elif mark >= 70:
        gp = 2
    elif mark >= 65:
        gp = 3
    elif mark >= 60:
        gp = 4
    elif mark >= 55:
        gp = 5
    elif mark >= 50:
        gp = 6
    elif mark >= 45:
        gp = 7
    elif mark >= 40:
        gp = 8
    else:
        gp = 9
    return gp
# print(getgradepoint(20))
# print(getgradepoint(40))
# print(getgradepoint(50))
# print(getgradepoint(60))
# print(getgradepoint(70))

def calL1R5(result):
    L1 = 0
    total = 0
    for key , value in result.items():
        if key == "English":
            L1 =  getgradepoint(value)
        elif key == "Higher Chinese":
            if getgradepoint(value) < L1:
                L1 = getgradepoint(value)
            else:
                L1 = L1
        else:
            total = total + getgradepoint(value)
    print(f"l1 : {L1}")
    print(f"r5 : {total}")
    L1R5 = L1 + total
    return L1R5
# test = {"English":71 ,"Higher Chinese":80 ,"Chemistry":63,"Geography":72,"Mathematics":60 ,"Physics":66 ,"Computing":70 }
# print(calL1R5(test))

score_template = {"English":0 ,"Higher Chinese":0 ,"Chemistry":0 ,"Geography":0 ,"Mathematics":0 ,"Physics":0 ,"Computing":0 }

for score in score_template:
    current_score = int(input(f"What is your score for {score}?: "))
    score_template[score] = current_score
# print(calL1R5(score_template))
with open("resultslip.txt", "w") as rf:
    for subject,score in score_template.items():
        rf.write(f"{subject:<15} {score:>8}\n")
    L1R5 = calL1R5(score_template)
    rf.write(f"ComputedL1R5:{L1R5}")