def split_sentence(word_string):  
    list_sentence = word_string.split()
    return list_sentence

def check_list(word, sentence):   #Defining function and parameters
    word_list = split_sentence(sentence)   #calling previous function
    if word in word_list:    #Existence check to find word
        return "Yes"   #Returning yes if found
    else:
        return "No"     #Returning no if not found

def reverse_sentence(word_string):   #Defining function and parameters
    word_list = split_sentence(word_string)   #Calling previous function
    reverse_sentence = ""
    for word in word_list:     #Looping through the word list for every word inside 
        reverse_sentence = word + " " + reverse_sentence     #Reverses the order of the words
    return reverse_sentence      #Returning reversed sentence
# print(reverse_sentence("the cat sat on the mat" ))

user_input = input("Input a string of words: ")   #Takes the users string of words as an input
word_check = input("What word do you want to search for?: ")     #checks what word they want to find
print(split_sentence(user_input))     #Calling previous function
print(reverse_sentence(user_input))     #Calling previous function
if check_list(word_check,user_input) == "Yes":
    print("Your word was found in the string")
else:
    print("Your word was not found in the string")