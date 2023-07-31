matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]

# Opción 1
suma = 0
for i in range(len(matrix)):
    suma += matrix[i][i]
print(suma)

# Opción 2
diagonal = []
for i in range(len(matrix)):
    diagonal.append(matrix[i][i])
print(sum(diagonal))

# Opción lista por comprensión
size = len(matrix)
main_diagonal = [matrix[i][i] for i in range(size)]
sum_diagonal = sum(main_diagonal)
print(sum_diagonal)
