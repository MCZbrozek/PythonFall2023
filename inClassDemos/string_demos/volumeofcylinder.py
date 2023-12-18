# Program: volumeofcylinder.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 14 Sep 2023
# Purpose: Calculate volume of cylinder  

# import math
# pi = math.pi
from math import pi as pi
# display header
print("Welcome to cylinder calc! ")
# Get radius
radius = float(input("Please enter the radius of cylinder base in UNITs: "))
# Get height
height = float(input("Please enter the height of cylinder in UNITs: "))
# Calculate pr2**2 (h)
volume_of_cylinder = round((pi * (radius**2)) * height, 2)
# display result
print("The volume of your cylinder is:", volume_of_cylinder, "UNITs cubed")
# Goodbye message 
print("Thank you for choosing cylinder calc for all of your cylinder calculation needs. ")

# with a format specifier 
format = "The colume of a cylinder with a height of %.2f mm and a radius of %.2f mm in cubic mm is %.2f."
items = (height, radius, volume_of_cylinder)
print(format % items)

# with PrintF
print(f"The volume of the cylinder with a height of {height:,.2f} mm and a radius of {radius:,.2f} mm in cubic mm is {volume_of_cylinder:,.3f}")