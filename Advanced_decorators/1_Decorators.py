# functions are first class citizen in python
# decorators helps in superboosting a function and add extra functionality


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("*******")
    return wrap_func

@my_decorator
def hello():
    print("Hello")

hello()

@my_decorator
def hello2(greeting, emoji=':()'):
    print(greeting, emoji)

hello2('hiiii')
