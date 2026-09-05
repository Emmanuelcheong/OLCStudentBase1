
# # Task 4
# # Open the file MASTERMIND.ipynb
# # Save the file as: # TASK4___.ipynb
# # (e.g. TASK4_S300_08_Jane Tan.ipynb)

# # The task is to identify and correct errors in program code so that the 
# # program works according to the given rules.

# # The following program creates and plays a game of Mastermind with the user.
# # Mastermind is a two-player code breaking game. Sam wrote the program 
# # using the following rules.
# #     • The computer will randomly generate a 4-digit code 'XXXX' where 
# #       X is between 1 and 8, inclusive.
# #     • Players will be given 10 tries to guess the code. 
# #       Each guess is an input of 'XXXX'.
# #     • For every guess:
# #         o if the player guesses correctly, the program will end with a 
# #           congratulatory message and state the number of tries taken.
# #         o otherwise, the program will provide feedback: a 'R' is given for 
# #           every correct digit that is in the correct position, and a 
# #          'W' is given for every correct digit in the wrong position.
# #     For example. Code = "1234" and Guess = "2764", the feedback will be 'RW'
# #     • After 10 tries, the correct code will be revealed to the user.

# # There are several syntax errors and logic errors in the program.

# import random

# # Game variables
# tries = 0
# guess = ''
# code = ''

# # Generate the code
# while i in range(4):
#     temp = random.randint(1,8)
#     code += temp

# # Gameplay
# while tries <= 10:
#     tries += 1
#     guess = input(f"Try #{tries}, enter code: ")
#     feedback = ''
#     # the following 2 lists as used to mark the positions
#     # of guess & code that has been process for feedback
#     guess_pos = (False,False,False,False)
#     code_pos = (False,False,False,False)

#     if guess == code:
#         print(f"Congratulations! You broke the code on try #(tries)")

#     # check for any correct digit in correct position
#     for i in guess:
#         if code[i] == guess[i]:
#             feedback += "R"
#             guess_pos[i] = True # mark this position as processed
#             code_pos[i] = True # mark this position as processed

#     # check for any correct digit in wrong position
#     for i in range(4):
#         if not guess_pos:
#             for x in range[4]:
#                 if not code_pos and code[x] == guess[i]:
#                     feedback += "W"
#                     code_pos[x] = True
#     print(f"Feedback: {feedback}")

# # Code reveal
# if tries == 10:
#     print(f"The code is {guess}. Better luck next time!")


# # Identify and correct the errors in the program so that it works correctly 
# # according to the rules above.
# # [10]