num = int(input('Please enter a whole number: '))
#Say positive negative or zero
if num > 0:
    print(num>0)
    print(f"Your number, \'{num}\' is a positive number :)")
elif num < 0:
    print(num<0)
    print(f"Your number, \'{num}\' is a negative number :(")
else:
    print(f"Your number, \'{num}\' is equal to zero")