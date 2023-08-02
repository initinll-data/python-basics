# int, str, bool are immutable

x = 1
print(id(x))

x = x + 1
print(id(x))

y = True
print(id(y))

y = False
print(id(y))

z = "Hello"
print(id(z))

z = "Hello-World"
print(id(z))

# list is mutable

a = [1, 2, 3]
print(id(a))

a.append(4)
print(id(a))
