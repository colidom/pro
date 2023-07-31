val1 = 7
val2 = 4
val3 = 9

if val1 < val2:
    if val1 < val3:
        min_value = val1
    else:
        min_value = val3
elif val2 < val3:
    min_value = val2
else:
    min_value = val3

print(min_value)
