for i in range(1,10):
    if(i<=5):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")
    else:
        for j in range(0,10-i):
            print("*",end=" ")
        print("\n")
    
