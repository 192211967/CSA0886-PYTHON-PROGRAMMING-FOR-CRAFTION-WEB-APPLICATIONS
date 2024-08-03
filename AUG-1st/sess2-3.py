def transpose_in_place(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)
print(transpose_in_place([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]))

