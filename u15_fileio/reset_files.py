
# file_creation.py
# Creates the text files needed for the File IO practice questions

files_data = {
    "q1_greeting.txt": "Hello and welcome to Python File IO.",
    
    "q3_diary.txt": "I went to school today.",
    
    "q4_fruits.txt": "apple\nbanana\norange\nmango",
    
    "q5_marks.txt": "75\n62\n88\n49\n91\n56",
    
    "q6_names.txt": "amir\nbeth\nchen\ndivya",
    
    "q7_temperatures.txt": "29\n31\n33\n28\n35\n30\n36",
    
    "q8_animal_names.txt": "cat,dog,rabbit,hamster",
    
    "q8_animal_sounds.txt": "meow,bark,squeak,peep",
    
    "q9_scores.txt": "56\n72\nabc\n91\n-4\n105\n68",
    
    "q10_expenses.txt": "Transport,12\nFood,8\nBooks,15\nTransport,10\nFood,6\nFood,9",
    
    "q11_sales.txt": "Pen,12,1.5\nBook,5,4.8\nEraser,20,0.6\nPencil,10,1.2\nRuler,3,2.5"
}



for file_name, file_content in files_data.items():
    file = open(file_name, "w")
    file.write(file_content)
    file.close()
    print(file_name + " created successfully")

print("All files have been created.")