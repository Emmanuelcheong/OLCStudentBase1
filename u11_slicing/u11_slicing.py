#Slicing works on list and strings
word = "SINGAPORE"
#Retrieve by a certain index
print(word[0])
#Slicing,start,stop,step >>>> range()

#retrieve SIN from SINGAPORE
print(word[:3])
#Retrieve GAP from SINGAPORE
print(word[3:6])
#retrieve last letter from SINGAPORE
print(word[-1])
#retrieve last letter from SINGAPORE
print(word[:-4])
#retrieve every other letter
print(word[::2])
#Reverse a word
print(word[::-1])