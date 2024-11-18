n=int(input("Enter the number whose multiplication table is to be printed:"))
limit=int(input("Enter the number of multiples to be found: "))
for i in range(1,limit+1):
    z=n*i
    print(n,"*",i,"=",z,"\n")
