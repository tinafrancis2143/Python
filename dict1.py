stud={"name":"Kuttan","age":20,"college":"cet","district":"kottayam"}
keys=list(stud.keys())
values=list(stud.values())
print(keys)
keys.sort()
print(keys)
print("{")
dict={}
for i in keys:
    dict[i]=stud[i]
print(dict)

keys.reverse()
print(keys)
dictrev={}
for i in keys:
    dictrev[i]=stud[i]
print(dictrev)
