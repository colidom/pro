decimal = 11
to_bin = []

while decimal != 0:
    module = decimal % 2
    quotient = decimal // 2
    to_bin.append(module)
    decimal = quotient

print(to_bin[::-1])
