#get 3 numbers from the user 
name = input("Please enter your name: ")
num1 = float(input("First number?: "))
num2 = float(input("Second number?: "))
num3 = float(input("Third number?: "))
# calculate them using using method 1
result1 = num1 + num2 / num3
# calculate them using using method 1
result2 = (num1 + num2) / num3
# display results
print("Use your number to calculate the result of this formula: num1 + num2 / num3")
print()
print("Well,", name, "This is your result", result1)
print()
print("Use your number to calculate the result of this formula: (num1 + num2) / num3")
print()
print(result2)