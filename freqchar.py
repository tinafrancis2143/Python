x=input("Enter the word")
y=input("Enter the character to be counted")
flag=0
for i in x:
    if(i==y):
        flag=flag+1
print(f"{y} appears {flag} times")
    
