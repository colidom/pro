matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]

suma = 0
for i in range(len(matrix)):
    suma += matrix[i][i]
print(suma)
