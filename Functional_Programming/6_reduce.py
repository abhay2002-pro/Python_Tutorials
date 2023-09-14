from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

def accumulator(acc, item):
    acc += item
    return acc

print(reduce(accumulator, my_list, 0))