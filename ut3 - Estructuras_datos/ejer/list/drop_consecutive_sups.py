elements = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
unique_elements = []
prev_element = None

for current_element in elements:
    if current_element != prev_element:
        unique_elements.append(current_element)
        prev_element = current_element

print(unique_elements)
