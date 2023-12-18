def get_denominatort_from_user():
    denominator = float(input("Please enter a number for the denominator: "))
    return denominator

def get_numerator_from_user():
    numerator = float(input("Please enter a number for the numerator: "))
    return numerator

def calc_result(denominator, numerator):
    result = numerator/denominator
    return result
    

do_another = 'y'
while do_another == 'y':    
    # Without the try/except block the code will return control to the command line, which is a security hazard. 
    try:
        numerator = get_numerator_from_user()
        denom = get_denominatort_from_user()
        result = calc_result(denom,numerator)
        print(result)
    except ZeroDivisionError:
        print(f"Error! Enter a denominator that is not zero!!")
    except ValueError:
        print(f"Error!! Numbers only please!! Don't make me tell you again")
    except Exception as exc:
        print(f"Critical error {exc}")

    do_another = input("Another (y/n)?")