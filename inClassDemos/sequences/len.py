numbers = [100,34,670, 45, 8954]
count_of_numbers = len(numbers)
print("There are", count_of_numbers, "numbers in list")

min_number = min(numbers)
print("The lowest number is", min_number, ".")

max_number = max(numbers)
print("The highest number is "+str(max_number)+".")

longest_number = len(str(max(numbers)))
print("The length of the longest number has "+str(longest_number)+"numbers")