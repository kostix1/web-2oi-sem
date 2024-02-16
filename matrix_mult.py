def matrix_mult(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Проверь матрицы")
    else:
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                matrix1[i][j] *= matrix2[i][j]
    print(matrix1)
