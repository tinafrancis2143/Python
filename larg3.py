x,y,z=input("Enter three different numbers: ").split()
if x>y and x>z:
    print(x,"is greatest")
elif y>x and y>z:
    print(y,"is greatest")
elif z>x and z>y:
    print(z,"is greatest")
