elements = [1, 1, 1, 1, 1, 1, 1]
equals = []
first_element = elements[0]

for current_element in elements[1:]:
    if current_element != first_element:
        print("Son distintos")
        break
else:
    print("Son iguales")
