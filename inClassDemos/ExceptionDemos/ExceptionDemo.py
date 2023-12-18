def get_denominatort_from_user():
    denominator = float(input("Please enter a number for the denominator: "))
    return denominator

def get_numerator_from_user():
    numerator = float(input("Please enter a number for the numerator: "))
    return numerator

def calc_result(denominator, numerator):
    if numerator != 0:
        result = denominator/numerator
    else:
        result = None
    return result

denom = get_denominatort_from_user()
numerator = get_numerator_from_user()
result = calc_result(denom,numerator)
print(result)