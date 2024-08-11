def transpose(a):
    c=[[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[j][i]
    for i in c:
        print(i)
transpose([[1,2],[4,5]])

