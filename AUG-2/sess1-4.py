def print_boolean_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]:
                print(" * ", end="")
            else:
                print("  ", end="")
        print()
print(print_boolean_matrix([[True, False, True],[False, True, False]]))
