# glocal refers to a global variable while nonlocal refers to a variable which is not glocal but is present in parent
x = "glocal"
def outer():
    # nonlocal x -> will throw error
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print(f"inner {x}")
    inner()
    print(f"outer {x}")

outer()