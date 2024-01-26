# Write lambda functions to find area of square, rectangle and triangle. 
area1=lambda a: a*a
area2=lambda l,b: l*b
area3=lambda b,h: 0.5*(b*h)
s=int(input("Enter the side of square : "))
print("Area of square : ",area1(s))
l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
print("Area of rectangle : ",area2(l,b))
b=int(input("Enter the base of triangle : "))
h=int(input("Enter the height of triangle : "))
print("Area of triangle : ",area3(b,h))