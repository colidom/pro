import sys

# En values tendremos una lista con los valores (como strings)
values = sys.argv[1:]

values = [int(v) for v in values]
avg = sum(values) / len(values)

print(avg)
