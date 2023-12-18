names=["Alice", "Beth", "Cecil", "Dee-dee", "Earl"]
print(names)
new_names=input("Type a name to add it to the list: ").title()
names.append(new_names)
print(names)

remove_names=input("Type a name to remove it from the list: ").title()
names.remove(remove_names)

names.sort()
print(names)

number_of_names = names.count("Mike")
print(number_of_names)

reverseNames = names.reverse()
print(reverseNames)