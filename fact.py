n=int(input("Enter the number(>=)whose factorial is to be found: "))
fact=1
if n==0 and n==1:
    fact=1
    print("factorial is ",fact)
else:
    for i in range(1,n+1,1):
        fact=fact*i
    print("factorial is ",fact)
