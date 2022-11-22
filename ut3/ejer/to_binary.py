decimal = 11
to_bin = []

while decimal != 0:
    module = decimal % 2
    to_bin.append(decimal % 2)
    decimal //= 2

to_bin = [str(i) for i in to_bin[::-1]]
to_bin = "".join(to_bin)
print(to_bin)
