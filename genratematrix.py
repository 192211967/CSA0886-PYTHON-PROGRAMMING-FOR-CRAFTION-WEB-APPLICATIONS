def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # Fill top row
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

# Test Case 1
n1 = 3
print(generateMatrix(n1))
# Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

# Test Case 2
n2 = 1
print(generateMatrix(n2))
# Output: [[1]]
