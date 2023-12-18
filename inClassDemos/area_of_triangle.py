# Program: area_of_triangle.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 05 Sept 2023
# Purpose: Calculate the area of a triangle given user's inputs. 
# Are of a triangle.

import math
#Ask the name of the user
name = input("What is your name?:")
print()
#Tell the user what this program does 
print("Hey,"+name+"!" "Welcome to Triangul-area, THE triangle area calculator")
print()
#Collect the units from the user
units = input("What units would you like to use?: ")
#Collect base from the user
base = float(input("What is the base length of your triangle in "+units+"?:"))
print()
#Collect height from the user
height = float(input("What is the height of your triangle in "+units+"?:"))
print()
#Calculate results
area = math.round((base * height)/2,3)
if int(area) - area == 0: area = int(area)
#Display the results
print("The area of your triangle is: ", area, units, "Squared")
print()
#Say thank you
print("Thank you,"+name+"for using Triangul-area, THE triangle area calculator")