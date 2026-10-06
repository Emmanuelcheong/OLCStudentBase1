
############################################################
# TASK 2 - REFINEMENT OF PROGRAM
############################################################

# The program allows a user to enter a word and stores the word in a list.


# word_list = []

# word = input("Enter a word containing at least 5 letters: ")
# word_list.append(word)



#------------------------------------------------------------
# Task 2.1 [4]
#------------------------------------------------------------

# Extend the program so that the word entered is validated
# before it is stored in the list.
#
# The program must:
# - check that the word contains at least 5 characters;
# - check that every character in the word is an alphabetic letter;
# - if the word is invalid, output a suitable message explaining why and
#   repeatedly ask the user to enter another word until a
#   valid word is entered;
# - convert the valid word to lower case before storing it
#   into a list named word_list.
# word_list = []
# while True:
#     word = input("Enter a word containing at least 5 letters: ")
#     flag = True
#     for char in word:
#         if not char.isalpha():
#             flag = False
#     if len(word) < 5:
#         flag = False
#     if flag:
#         word_list.append(word.lower())
#         break
#     else:
#         continue




#------------------------------------------------------------
# Task 2.2 [5]
#------------------------------------------------------------

# Copy and paste your program from Task 2.1.
#
# Extend the program so that it:
# - asks the user whether another word is to be entered
#   after each valid word is stored;
# - accepts Y to enter another word and N to stop;
# - continues to apply the validation rules from Task 2.1
#   to every word entered;
# - stores every valid word in word_list;
# - outputs each word from the completed word_list one by one
#   when the user chooses to stop.
#
# You can assume that the user will only enter Y or N when asked
# whether another word is to be entered.
# word_list = []
# while True:
#     word = input("Enter a word containing at least 5 letters: ")
#     flag = True
#     for char in word:
#         if not char.isalpha():
#             flag = False
#     if len(word) < 5:
#         flag = False
#     if flag:
#         word_list.append(word.lower())
#         user_input = input("Do you want to continue? (Y or N)")
#         if user_input == "Y":
#             break
#         else:
#             continue
#     else:
#         continue






#------------------------------------------------------------
# Task 2.3 [6]
#------------------------------------------------------------

# Copy and paste your program from Task 2.2.
#
# A dictionary is required to count the number of times each
# vowel occurs in all the words stored in word_list.
#
# Use the following dictionary:

vowel_count = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

# Extend the program so that it:
# - checks every character in every word stored in word_list;
# - increases the correct value in vowel_count whenever a
#   vowel is found;
# - outputs the completed vowel_count dictionary;
# - outputs the count for each of the five vowels using
#   suitable output messages.
word_list = []
while True:
    word = input("Enter a word containing at least 5 letters: ")
    flag = True
    for char in word:
        if not char.isalpha():
            flag = False
    if len(word) < 5:
        flag = False
    if flag:
        word_list.append(word.lower())
        user_input = input("Do you want to continue? (Y or N)")
        if user_input == "N":
            break
        else:
            continue
    else:
        continue
for word in word_list:
    for char in word:
        for vowel,count in vowel_count.items():
            if char == vowel:
                vowel_count[vowel] += 1
print(vowel_count)

