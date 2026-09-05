
# Task 4
# Open the file MASTERMIND.ipynb
# Save the file as: # TASK4___.ipynb
# (e.g. TASK4_S300_08_Jane Tan.ipynb)

# The task is to identify and correct errors in program code so that the 
# program works according to the given rules.

# The following program creates and plays a game of Mastermind with the user.
# Mastermind is a two-player code breaking game. Sam wrote the program 
# using the following rules.
#     • The computer will randomly generate a 4-digit code 'XXXX' where 
#       X is between 1 and 8, inclusive.
#     • Players will be given 10 tries to guess the code. 
#       Each guess is an input of 'XXXX'.
#     • For every guess:
#         o if the player guesses correctly, the program will end with a 
#           congratulatory message and state the number of tries taken.
#         o otherwise, the program will provide feedback: a 'R' is given for 
#           every correct digit that is in the correct position, and a 
#          'W' is given for every correct digit in the wrong position.
#     For example. Code = "1234" and Guess = "2764", the feedback will be 'RW'
#     • After 10 tries, the correct code will be revealed to the user.

# There are several syntax errors and logic errors in the program.

import random

# Game variables
tries = 0
guess = ''
code = ''

# Generate the code
for i in range(4):      #1: Syntax error, while loop should be a for loop
    temp = random.randint(1,8)
    code += str(temp) #2: Logic error, to concatanate should convert to string
print(code)
# Gameplay
while tries < 10:    #3: Logic error, should be less than 10 and not equals to
    tries += 1
    guess = input(f"Try #{tries}, enter code: ")
    feedback = ''
    # the following 2 lists as used to mark the positions
    # of guess & code that has been process for feedback
    guess_pos = [False,False,False,False]     #4: Both are tuples and c=should be lists so they can be modified later on
    code_pos = [False,False,False,False]

    if guess == code:
        print(f"Congratulations! You broke the code on try #{tries}")   #5: Logic Error, use of wrong brackets means the number of tries is not shown
        break   #11: Logic error, code should end after the guess matches the code
    # check for any correct digit in correct position
    for i in range(len(guess)):     #6: Logic error, i should be an integer and not a string
        if code[i] == guess[i]:
            feedback += "R"
            guess_pos[i] = True # mark this position as processed
            code_pos[i] = True # mark this position as processed

    # check for any correct digit in wrong position
    for i in range(4):
        if not guess_pos[i]:      #7: Logic error, should be only an item and not the whole list
            for x in range(4):     #8: Syntax error, code should use () instead of []
                if not code_pos[x] and code[x] == guess[i]:     #9: Logic error, should compare between the position of x in the list cpde_pos
                    feedback += "W"
                    code_pos[x] = True
    print(f"Feedback: {feedback}")

# Code reveal
if tries == 10:
    print(f"The code is {code}. Better luck next time!")   #10: Logic error, should give the anwer and not the guess


# Identify and correct the errors in the program so that it works correctly 
# according to the rules above.
# [10]