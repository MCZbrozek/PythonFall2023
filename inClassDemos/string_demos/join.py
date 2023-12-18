# seq = [1,2,3,4,5,6]
seq = ["1","2","3","4","5","6"] # Must be strings to use join
sep = "+"
print(sep.join(seq))

dirs = '','usr','bin', 'env' # This is a tuple by default since we didn't use ()
print('/'.join(dirs)) 

print('wah \n\n\n\n wah \n\n\n\n wah')
print('wah \t\t\t\t wah \t\t\t\t wah')

print('c:' + "\\".join(dirs))