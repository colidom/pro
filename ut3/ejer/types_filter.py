lista = [1, 2, 3, 4, True, "Hola Mundo"]
l_int = []
l_str = []
unknown_type = []

for i in lista:
    if type(i) == int:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
    else:
        unknown_type.append(i)

print(l_int)
print(l_str)
print(unknown_type)
