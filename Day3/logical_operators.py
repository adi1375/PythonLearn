a = 10
b = 20
c = 30
d = 40

# and
print("AND")
print(a > b and a > c)
print(a > b and a < c)
print(a < b and a > c)
print(a < b and a < c)
print(a < b and c)
print(a > b and c and d)
print()

# or
print("OR")
print(a > b or a > c)
print(a > b or a < c)
print(a < b or a > c)
print(a < b or a < c)
print(a < b or c)
print(a > b or c or d)
print()

# not
print("NOT")
print(not a < b)
print(not a > b)
