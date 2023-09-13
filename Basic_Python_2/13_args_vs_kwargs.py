# kwargs are keyword arguments

def super_func(*args, **kwargs):
    # print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, 6, 7, 8, 9, num1 = 5, num2 = 10) )
