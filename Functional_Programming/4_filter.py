my_list = [1,2,3,4,5,6]

def check_odd(item):
    return item%2

print(list(filter(check_odd, my_list)))