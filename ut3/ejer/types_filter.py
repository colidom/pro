lista = [1, 2, 3, 4, True, "Hola Mundo"]
l_int = []
l_str = []
b_type = []

for i in lista:
    if type(i) == int:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
    elif type(i) == bool:
        b_type.append(i)
    else:
        b_type.append(i)

print(l_int)
print(l_str)
print(b_type)
