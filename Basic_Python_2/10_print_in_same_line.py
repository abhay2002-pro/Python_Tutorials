my_list = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
]
for row in my_list:
    for item in row:
        if(item == 1):
            print("*", end='')
        else:
            print(" ", end='')
    print('')