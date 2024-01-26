# Create a package graphics with modules rectangle, circle and subpackage 3D-graphics with modules cuboid and sphere. Include methods 
# to find area and perimeter of respective figures in each module. Write 
# programs to find the area and perimeter of figures by different importing 
# statements. (Include selective import of modules and import * 
# statements).


from graphics import rectangle, circle
from graphics.3Dgraphics import cuboid,shpere
print("Area and Perimeter of Rectangle")
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
print("Area of the Rectangle : ",Rectangle.area(l,b),"\nPerimeter of the Rectangle : ",Rectangle.perimeter(l,b))
print("Area and Perimeter of Circle")
r=int(input("Enter the radius : "))
print("Area of the Circle : ",Circle.area(r),"\nPerimeter of the Circle : ",Circle.perimeter(r))
print("Surface area and Volume of Cuboid")
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
h=int(input("Enter height : "))
print("Surface area of the Cuboid : ",Cuboid.surface_area(l,b,h),"\nVolume of the Cuboid : ",Cuboid.volume(l,b,h))
print("Surface area and Volume of Sphere")
r=int(input("Enter the radius : "))
print("Surface area of the Sphere : ",Sphere.surface_area(r),"\nVolume of the Sphere : ",Sphere.volume(r))