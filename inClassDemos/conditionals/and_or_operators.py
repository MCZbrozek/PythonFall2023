number = int(input("Please enter a number between 1 & 10:"))
if number <= 10 and number >= 1:
        print("Great!")   
else:
    print('Wrong!!!')

# Boolean 'and' operator
# T and T => T
# T and F => F
# F and T => F
# F and F => F

number = int(input("Please enter a number between 1 & 10:"))
if number <= 10 or number >= 1:
        print("Great!")   
else:
    print('Wrong!!!')
# Boolean 'or' operator
# T or T => T
# T or F => T
# F or T => T
# F or F => F
