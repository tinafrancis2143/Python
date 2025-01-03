x=int(input("Enter first number: "))
y=int(input("Enter second bumber: "))

if(x<y):
    for i in range(x,0,-1):
         if(x%i==0 and y%i==0):
            print("GCD is",i)
            break
elif(y<x):
    for i in range(y,0,-1):
        if(x%i==0 and y%i==0):
            print("GCD is",i)
            break
else:
    print("GCD is",x)
