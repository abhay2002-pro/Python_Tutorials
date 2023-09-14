# Find duplicates in list

some_list = ['a', 'b', 'c', 'd', 'a', 'b']

duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))

print(duplicates)
