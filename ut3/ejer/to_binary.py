decimal = 11
modules = []

while decimal != 0:
    module = decimal % 2
    quotient = decimal // 2
    modules.append(module)
    decimal = quotient

print(modules[::-1])
