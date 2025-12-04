# #TEXT FILES - Files that contain texts
# #How to open/read/write a file

# #How to create a file
# with open("test1.txt", "w") as fobj:  # "w" for write, "r" for read, "a" to append 
#     fobj.write("Bye world\n")
#     fobj.write("lemon\n")
#     fobj.write("leron\n")
#     fobj.write("heron\n")
# #How to read from a file
# with open("test1.txt", "r") as fobj:
#     contents = fobj.read()  #Read entire file and returns as a file

#Read file and choose a random item from file
# #.read() being a string makes it harder
# import random
# with open("test1.txt" ,"r") as fobj:
#     contents = fobj.readlines()
# rananimal = random.choice(contents).strip("\n")
# print(f"Today I saw a {rananimal} at the zoo")


#CSV  Comma seperated value
# with open("test1.txt", "r") as fobj:
#     contentstr = fobj.read().split(",")
# print(contentstr)