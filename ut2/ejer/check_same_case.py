a = "a"
b = "g"

if not a.isalpha() or not b.isalpha():
    result = -1
if a.islower() and b.islower() or a.isupper() and b.isupper():
    result = 1
else:
    result = 0

print(result)
