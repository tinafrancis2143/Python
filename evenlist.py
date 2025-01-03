number_list=[]
for list in range (1,101):
    number_list.append(list)
print(number_list,end="")

even_list=[]
for list in number_list:
    if list%2==0:
        even_list.append(list)
print("\n\n\n\n",even_list)        
