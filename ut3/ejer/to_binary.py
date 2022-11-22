decimal = 11
to_bin = []

while decimal != 0:
    module = decimal % 2
    to_bin.append(decimal % 2)
    decimal //= 2

print(to_bin[::-1])
