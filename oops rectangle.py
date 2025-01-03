class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
       
    def perimeter(self):
        return(2*(self.length+self.breadth))
        
        
    def area(self):
        return(self.length*self.breadth)
        
        
rect1=Rectangle(4,5)
rect2=Rectangle(5,10)
print("Perimeter of rectangle 1:",rect1.perimeter())
print("Area of rectangle 1:",rect1.area())
print("Perimeter of rectangle 2:",rect2.perimeter())
print("Area of rectangle 2:",rect2.area())

if rect1.area()>rect2.area():
    print("first rectangle is largest")
elif rect1.area()<rect2.area():
    print("second rectangle is largest")
else:
    print("both rectangles have same area")




        
        
        
