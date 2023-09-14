# Generators are subset of iterable
# Every geenrator such thta range is a iterable
# Every iterable while isn't a generator like list
# Generators are generally functions

def generator_function(num):
    for i in range(0, num):
        yield i

for item in generator_function(10):
    print(item, end = '')

print('')
g = generator_function(10)
print(next(g))
print(next(g))
print(next(g))