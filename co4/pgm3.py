
# Create a class Rectangle with private attributes length and width. Overload ‘<’  operator to compare the area of 2 rectangles.

class Rectangle:
 def __init__(self, length, width):
    self._length = length
    self._width = width
 def area(self):
    return self._length * self._width
 def __lt__(self, other):
    return self.area() < other.area()
    print("First rectangle: ")
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
rectangle1 = Rectangle(l, b)
print("Second rectangle: ")
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
rectangle2 = Rectangle(l, b)
if rectangle1 < rectangle2:
    print("Area of Rectangle 1 is smaller than the area of Rectangle 2.")
elif rectangle1 > rectangle2:
    print("Area of Rectangle 1 is larger than the area of Rectangle 2.")
else:
    print("Both rectangles have the same area.")