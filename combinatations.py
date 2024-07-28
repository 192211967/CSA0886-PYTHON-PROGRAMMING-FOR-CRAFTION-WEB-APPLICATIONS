def combine(n, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path)
            return
        for i in range(start, n + 1):
            backtrack(i + 1, path + [i])

    result = []
    backtrack(1, [])
    return result

# Test Case 1
n1, k1 = 4, 2
print(combine(n1, k1))
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Test Case 2
n2, k2 = 1, 1
print(combine(n2, k2))
# Output: [[1]]
