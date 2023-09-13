# [start:stop]
selfish = '01234567'
print(selfish[0:2])

# [start:stop:steps]
print(selfish[0:8:2])

# [start:]
print(selfish[1:])

# #[:stop]
print(selfish[:7])

# [start::step]
print(selfish[1::2])

# Negative indices

print(selfish[-1])

print(selfish[::-1])

# Deep copy
new_selfish = selfish[:]
print(new_selfish)
