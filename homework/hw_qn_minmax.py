
###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here
highest_emp = ""
lowest_emp = ""
total = 0
count = 0
non_performers = {}
highest_score = performance_scores["Alice"]
lowest_score = performance_scores["Alice"]
for name,performance in performance_scores.items():
    total += performance
    count += 1  
    if performance > highest_score:
        highest_score = performance
        highest_emp = name
    if performance < lowest_score:
        lowest_score = performance
        lowest_emp = name
    if performance < 50:
        non_performers[name] = performance
print(f"The highest performer is {highest_emp}")
print(f"The lowest performer is {lowest_emp}")
print(f"The average performance score is {total/count}")
for name, score in non_performers.items():
    print(f"{name}, you are underperforming")
