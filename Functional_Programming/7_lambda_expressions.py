# lambda expressions are used for functions which are going to be used only once

from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item%2!=0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list, 1))
