A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

elem00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
elem01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
elem02 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
elem03 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

result = [[elem00, elem01], [elem02, elem03]]
print(result)


""" for matrix1, matrix2 in zip(A, B):
    print(matrix1, matrix2)
    # print(matrix2)
 """
