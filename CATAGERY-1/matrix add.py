def mul(a,b):
    c=[[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(b)):
            c[i][j]=a[i][j] + b[i][j]
    for i in c:
        print( i )
print(mul([[1,2],[5,3]],[[2,3],[4,1]]))
