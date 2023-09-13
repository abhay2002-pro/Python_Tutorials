user = {
    'basket': [1,2,3],
    'greet': 'hello'
}

# print(user['age']) -> throw errors
print(user.get('age'))

print(user.get('age', 55))

#  Another way of creating dictionary

user2 = dict(name='JohnJohn')
print(user2)

print('basket' in user2)
print('name' in user2)

print('name' in user2.keys())
print('JohnJohn' in user2.values())

print(user.items())

user3 = user2.copy()
print(user3)

print(user.pop('basket'))

user.update({'backet': 12})
print(user)