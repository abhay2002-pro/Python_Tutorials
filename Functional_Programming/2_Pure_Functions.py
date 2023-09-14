# Produces same output for same input everytime
# Pure functions should'nt produce side effects.
# Side effects are effects to outside world.  

def multiply_by2(li): # This is a pure function
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

def multiply_by2_ext(li): # Not a pure function as the output is provided to the display
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)


print(multiply_by2_ext([1,2,3]))
