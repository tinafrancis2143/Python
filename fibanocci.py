n=int(input("Enter the number of terms to be printed: "))
def fib(x):
    a=0
    b=1
    print("0\n1")
    for i in range (1,n-1,1):
         c=a+b
         print(c)
         a=b
         b=c 
if(n==1):
    print("0")
elif(n==2):
    print("0\n 1")
elif(n>2):
    fib(n)
