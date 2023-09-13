li = [1, 2, 3, 4, 5, 6]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# list is a data structure

print(li[-1::-1])

# lists are mutable

li[3] = 10
print(li)

# copy list
li3 = li # shallow copy
li3 = li[:] # deep copy