myFile = open("file1.txt")
myList =[]
for lines in myFile:
    myList.append(lines)

print(myList)