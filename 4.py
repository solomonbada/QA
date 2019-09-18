#Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
#r = float(input ("Input the radius of the circle : "))
#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


radius = float(input("Please enter radius of cirlce: "))

area = pi * radius**2

print("Radius of circle: " + str(radius))
print("Area of Circle: " + str(area))