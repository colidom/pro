elements = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

flat_list = []

for element in elements:
    if type(element) == list:
        flat_list.extend(element)
    else:
        flat_list.append(element)
print(flat_list)
