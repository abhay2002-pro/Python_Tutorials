def say_hello():
    print("Hello")

say_hello()

# parameters vs arguments
def say(name): # parameters 
    print("Hello " + name)

say('Abhay') # positional arguments
say(name='Abhay') # keyword arguments (order doesn't matter)