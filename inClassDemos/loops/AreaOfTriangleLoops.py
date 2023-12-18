import math
#Ask the name of the user
name = input("What is your name?:")
print()
#Tell the user what this program does 
print("Hey,"+name+"!" "Welcome to Triangul-area, THE triangle area calculator")
print()
# ---- All the code was placed in the loop below -----
doAnother = 'y'
while doAnother == 'y':
    #Collect the units from the user
    units = input("What units would you like to use?: ")
    #Collect base from the user
    base = float(input("What is the base length of your triangle in "+units+"?:"))
    print()
    #Collect height from the user
    height = float(input("What is the height of your triangle in "+units+"?:"))
    print()
    #Calculate results
    area = round((base * height)/2,3)
    if int(area) - area == 0: area = int(area)
    #Display the results
    print("The area of your triangle is: ", area, units, "Squared")
    print()
    doAnother = input('Do another (y/n)?')
    print()
    # ----- End of loop -----
#Say thank you
print("Thank you,"+name+"for using Triangul-area, THE triangle area calculator")