n=int(input("enter a year: "))
if(n%100==0):
    if(n%400==0):
        print("year is leap year")
    else:
        print("year is not a leap year")
else:
    if(n%4==0):
        print("year is leap year")
    else:
        print("year is not leap year")
