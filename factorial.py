n=int(input("Enter the number whose factorial is to be found: "))
def fact(a):
    for i in range(a-1,0,-1):
        a=a*i
    print(f"Factorial of {n} is {a}")

if(n==0 or n==1):
    print("Factorial of",n,"is 1")
elif(n>1):
    fact(n)
else:
    print("Factorial cannot be found")
