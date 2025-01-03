stud1={"name1":"Kuttan","age1":20.99,"college1":"cet","district1":"kottayam"}
stud2={"name2":"Tina","age2":21,"college2":"cet","district2":"Thrissur"}

keys1=list(stud1.keys())
keys2=list(stud2.keys())
print(stud1)
print("\n",stud2)
stud={}
for i in keys1:
    stud[i]=stud1[i]
for i in keys2:
    stud[i]=stud2[i]
print("\n\n",stud)


