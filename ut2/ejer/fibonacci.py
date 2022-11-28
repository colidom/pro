a = 0
b = 1
print(a)
print(b)

for _ in range(98):
    r = a + b
    a = b
    b = r
    print(r)
