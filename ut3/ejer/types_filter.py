lista = [1, 2, 3, 4, True, "Hola Mundo", 3.14]
l_int = []
l_str = []
b_type = []
unknown_type = []

for i in lista:
    if type(i) == int:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
    elif type(i) == bool:
        b_type.append(i)
    else:
        unknown_type.append(i)

print(f"Entero: {l_int}")
print(f"String: {l_str}")
print(f"Booleano: {b_type}")
print(f"Desconocido: {unknown_type}")
