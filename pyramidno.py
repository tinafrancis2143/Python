n=int(input("Enter the number of steps to be printed: "))
for i in range(0,n):
    for j in range(0,i+1):
        a=(j+1)*(i+1)
        print(a,end=" ")
    print("\n")
