def calculate_fibs(num):
    '''Returns a fibonaci seq with num elements The parameter must be of type int.'''
    fibs = [0,1]
    for i in range(num - 2):
        new_number = fibs[-2]+fibs[-1]
        fibs.append(new_number)
    return fibs

result = calculate_fibs(8)
print(result)

numbers_desired = int(input("Yo, how many numbs?: "))
# You can't just print result, the result needs to be placed in a variable.
fib_numbs = calculate_fibs(numbers_desired)

print(fib_numbs)