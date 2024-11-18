x=int(input("Enter first number"))
y=int(input("Enter second number"))
choice=int(input("Enter 1 for addition,2 for subtraction,3 for multiplication and 4 for division"))
if choice==1:
    z=x+y
elif choice==2:
    z=x-y
elif choice==3:
    z=x*y
elif choice==4:
    z=x/y
else:
    print("Wrong Choice")
print("Result is",z)
