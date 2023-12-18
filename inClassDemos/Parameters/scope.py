def myFunction():
    #--Function Scope -- 
    a = 3
    b = 4
    print(x)
    print(y)

def myOtherFunction():
    c = 5
    d = 6
    print(a) 
    print(b)

# -- Main Scope --
x = 1
y = 2
myFunction()
print(a)
print(b)

