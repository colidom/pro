elements = [1, 1, 1, 1, 1, 1, 1]
equals = []
prev_element = elements[0]

for current_element in elements:
    if current_element != prev_element:
        equals.append(current_element)

    print(current_element)
    # print(len(elements))
    # if len(elements) == len(equals):
    #     print("Son iguales")
    # else:
    #     print("Son distintos")
