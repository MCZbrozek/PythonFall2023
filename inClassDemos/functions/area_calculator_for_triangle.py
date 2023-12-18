#Progam: area_calculator_for_triangle.py
#Programmer: Mike Zbrozek(mzbrozek1@cnm.edu)
#Date 10/3/2023
#Purpose: Calculate are of triangle from user inputs

# -- Function Defs --
def display_header():
    print('Welcome to the the super triangle area calculator!!\n')

def get_base_from_user():
    base = float(input('Please enter base in feet: '))
    return base

def get_height_from_user():
    height = float(input('Please enter a height length in feet: '))
    return height

def calcuate_triangle_area(base_from_user, height_from_user):
    triangle_area = (base_from_user * height_from_user) / 2 
    return triangle_area

def display_result(base_from_user, height_from_user, area_result):
    print(f"The triangle with base of {base_from_user} feet, and a height of {height_from_user} feet, has an area of {area_result} feet^2. ")

def say_thankyou():
    print("So kind of you to use our amazing caluculator. Have a blessed day")

# def run_again():
#     while True:
#         user_response = input("Type 'y' to run again 'n' to exit")
#         if user_response == 'y':
#             get_base_from_user()
#             get_height_from_user()
#             calcuate_triangle_area()
#             display_result(base_from_user, height_from_user, area_result)
#         else:
#             say_thankyou()
#             break


# -- main --
# Display header
display_header()
# get base from user
base_from_user = get_base_from_user()
# get height from user
height_from_user = get_height_from_user()
# calculate area
area_result = calcuate_triangle_area(base_from_user, height_from_user)
# display result
display_result(base_from_user, height_from_user, area_result)
# run again 
# run_again()

