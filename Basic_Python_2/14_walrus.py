a = 'hellllllllloooooooooooo'

if(len(a) > 10):
    print(f"too long {len(a)} elements")

# len(a) is calculated twice above

if((n := len(a)) > 10):
    print(f"too long {n} elements")