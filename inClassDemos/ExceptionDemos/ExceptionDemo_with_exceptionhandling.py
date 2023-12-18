def get_denominatort_from_user():
    denominator = float(input("Please enter a number for the denominator: "))
    return denominator

def get_numerator_from_user():
    numerator = float(input("Please enter a number for the numerator: "))
    return numerator

def calc_result(denominator, numerator):
    result = denominator/numerator
    return result
    

do_another = 'y'
while do_another == 'y':    
    # Without the try/except block the code will return control to the command line, which is a security hazard. 
    try:
        denom = get_denominatort_from_user()
        numerator = get_numerator_from_user()
        result = calc_result(denom,numerator)
        print(result)
    except:
        print("Critical ERROR!! WORLD IS ENDING!!!!")

    do_another = input("Another (y/n)?")