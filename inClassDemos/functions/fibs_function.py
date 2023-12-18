def fibs(num):
    fibs = [0,1]
    for i in range(num - 2):
        new_number = fibs[-2]+fibs[-1]
        fibs.append(new_number)
    print(fibs)

fibs(8)