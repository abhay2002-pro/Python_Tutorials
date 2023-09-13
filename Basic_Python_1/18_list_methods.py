li = [1, 2, 3, 4, 5]

print(len(li))

# adding
li.append(6)
print(li)

li.insert(1, 10)
print(li)

li.extend([100, 110])
print(li)

# removing
li.pop()
print(li)

deleted = li.pop(0)
print(deleted)
print(li)

li.remove(100)
print(li)

li.clear()
print(li)

# find
li = [1,2,3,4,5]
print(li.index(2))

li.insert(4, 1)
print(li)

print(li.index(1, 2, 5))

print(9 in li)

print(li.count(1))

li.sort()
print(li)

li.append(0)

li2 = sorted(li)
print(li2)

li2.reverse()
print(li2)