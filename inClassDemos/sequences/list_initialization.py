# my_empty_list = []
# my_empty_list[5] = 55
# print(my_empty_list) <-- Produces an error 

better_way = [None] * 10
print(better_way)
better_way[5] = 55
print(better_way)