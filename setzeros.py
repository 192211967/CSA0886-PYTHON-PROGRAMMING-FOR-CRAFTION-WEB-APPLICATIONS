def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use the first row and column to mark zero rows and columns
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set matrix elements to 0 based on markers in the first row and column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set the first row to 0 if there was any zero initially
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Set the first column to 0 if there was any zero initially
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0

# Test Case 1
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix1)
print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# Test Case 2
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix2)
print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
