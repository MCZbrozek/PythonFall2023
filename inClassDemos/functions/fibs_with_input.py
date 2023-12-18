fibs = [0,1]
num = int(input('How many fib numbers'))
for i in range(num - 2):
    new_number = fibs[-2]+fibs[-1]
    fibs.append(new_number)
print(fibs)