lista = [1, 2, 3, 4, True, "Hola Mundo", 3.14]
int_type = []
str_type = []
b_type = []
unknown_type = []

for i in lista:
    if type(i) == int:
        int_type.append(i)
    elif type(i) == str:
        str_type.append(i)
    elif type(i) == bool:
        b_type.append(i)
    else:
        unknown_type.append(i)

print(f"Entero: {int_type}")
print(f"String: {str_type}")
print(f"Booleano: {b_type}")
print(f"Desconocido: {unknown_type}")
