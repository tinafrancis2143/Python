class Rectangle:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def get_area(self):
        return self.__width * self.__length

    def __lt__(self, other):
        return self.get_area() < other.get_area()

print("Enter the dimensions of the first rectangle:")
width1 = int(input("Width: "))
length1 = int(input("Length: "))
print("Enter the dimensions of the second rectangle:")
width2 = int(input("Width: "))
length2 = int(input("Length: "))
rectangle1 = Rectangle(width1, length1)
rectangle2 = Rectangle(width2, length2)
if rectangle1 < rectangle2:
    print("Rectangle 1 is smaller than rectangle 2")
else:
    print("Rectangle 2 is smaller than rectangle 1")