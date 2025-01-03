import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant term: "))
print(f"The quadratic equation is {a}x^2+{b}x+{c}")
x=b*b-4*a*c
y=math.sqrt(x)
var1=-b+y
var2=-b-y
root1=var1/(2*a)
root2=var2/(2*a)
print("Roots of the quadratic equation are",root1,root2)
