# how to split a string into a list without using split()

colors = "red,green,blue,yellow,orange,black,white"
# objective = ["red","green","blue","yellow","orange","black","white"]

colorlist = []
tempword = ""
for char in colors:
    if char == ",":
        colorlist.append(tempword)
        tempword = ""
        print(colorlist)
    else:
        tempword = tempword + char
        print(tempword)

# manually add the last word
colorlist.append(tempword)
print(colorlist)