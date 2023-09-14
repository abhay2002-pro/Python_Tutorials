my_list = [(1, 2), (3, 4), (5, 6)]

# sort using second element
my_list.sort(key = lambda x: x[1])
print(my_list)