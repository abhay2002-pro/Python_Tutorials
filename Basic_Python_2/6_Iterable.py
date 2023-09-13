# An DS that can be iterated over.
#list, dictionary, tuple, set, string

user = {
    'name': 'Goelm',
    'age': 5006
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for key, value in user.items():
    print(str(key) + " "  + str(value))