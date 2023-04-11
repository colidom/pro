v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

result = 0
for num_v1, num_v2 in zip(v1, v2):
    result += num_v1 * num_v2

print(result)
