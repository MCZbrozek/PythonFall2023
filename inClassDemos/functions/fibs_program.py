fibs = [0,1]
for i in range(8):
    new_number = fibs[-2]+fibs[-1]
    fibs.append(new_number)
print(fibs)

while len(fibs) < 20:
    new_number = fibs[-2]+fibs[-1]
    fibs.append(new_number)
print(fibs)