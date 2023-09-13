dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : [3, 4, 5]
}

print(dictionary['b'])
print(dictionary)

my_list = [
    {
        'a' : 1,
        'b' : 2
    }, 
    {
        'c': 3,
        'd': 5
    }
]

print('a' in my_list)
print(my_list[0]['a'])

# Keys need to be immutable - lists cannot be a key but string can be

dictionary = {
    'string': 123
}
print(dictionary['string'])

dictionary = {
    'string': 123,
    'string': 12
}
print(dictionary['string'])
