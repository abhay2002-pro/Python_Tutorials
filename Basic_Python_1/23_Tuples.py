my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# my_tuple[1] = 'z' -> throws error as tuples are also immutable

print(my_tuple[2])

dictionary = {
    (1,2) : [1,2,3]
}

print(dictionary[(1, 2)]) 

new_tuple = my_tuple[1:5]
print(new_tuple)

x,y,z, *other = (1, 2, 3, 4, 5)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))

