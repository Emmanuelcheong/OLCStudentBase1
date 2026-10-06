#------------------------------------------------------------
# Exercise 14: Pair Two Lists 
# Print "Alice: 85", "Ben: 73", etc. by pairing names with marks.
# Data:
names = ["Alice", "Ben", "Carmen", "Dylan"]
marks = [85, 73, 91, 66]
dict = {}
for i in range(len(names)):
    name = names[i]
    mark = marks[i]
    dict[name] = mark
print(dict)