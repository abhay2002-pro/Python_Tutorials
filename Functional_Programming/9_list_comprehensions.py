# list, set, dictionary comprehension

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# better way if doing above using comprehension

my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num*2 for num in range(0, 10)]
print(my_list2)

my_list3 = [num for num in my_list2 if num%2 == 0]
print(my_list3)
