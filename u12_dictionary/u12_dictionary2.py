###########################################################
# Part 2. IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# Task 1: Identify and print the name of the highest scoring student.
# highest_score = 0
# highest_student = ""
# for students,scores in students.items():
#     if scores> highest_score:
#         highest_score = scores
#         highest_student = students
# print(f"The highests scoring student is {highest_student} with a score of {highest_score}")

# #------------------------------------------------------------
# Task 2: Calculate and display the name and score of students scoring above 80. 
	  #Display the total number of students who scored above 80.
# bar_score = 80
# high_student = 0
# for students,scores in students.items():
#     if scores >= bar_score:
#         print(f"{students} : {scores}")
#         high_student += 1
# print(f"The total amount of students who got over 80 is {high_student}")



#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.

# for students_name,scores in students.items():
#     students[students_name] = scores + 5

# print(students)

# for name in students:
#     students[name] = students[name] + 5




###################################
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Available", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies, status Available.
# books["To Kill A Mockingbird"] = {"status": "Available", "copies": 3}

#------------------------------------------------------------
# Task 2: Update the status of the books to "Checked Out" if all copies are borrowed.
for bookname, status in books.items():
   if status["copies"] <= 0:
      status["status"] = "Checked Out"
print(books)
#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.

for bookname , status in books.items():
   if status["status"] == "Available":
        copy_count = status["copies"]
        print(f"{bookname} is available with {copy_count} copies")
        