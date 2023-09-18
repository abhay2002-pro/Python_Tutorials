import re 

string = 'search inside of this text please!'

print(string.count('search'))

print(re.search('this', string)) # gives index as well

a = re.search('a', string)
print(a)
print(a.span())
print(a.start())

# Making more advanced

pattern = re.compile('this')
string = 'search this inside of this text please!'

a = pattern.search(string)
print(a.group())
print(a)


# find all instanced

b = pattern.findall(string)
print(b)