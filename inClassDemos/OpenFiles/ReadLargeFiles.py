f = open("nibrAbqCodes.csv", 'r')
line_num = 0
while True:
    line = f.readline()
    if not line: break
    line_num += 1
    print(line.strip()) 
    if line_num%5 == 0:
        input('Press enter to continue')
f.close()