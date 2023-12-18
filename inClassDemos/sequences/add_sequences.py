list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = list1 + list2
print(list3)

str1 = "Hello "
str2 = "World!"
str3 = str1 + str2
print(str3)

result = list1 + list(str1)
print(result)
result1 = str(list1) + str1
print(result1)