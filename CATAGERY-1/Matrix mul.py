def mul(a,b):
    c=[[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                c[i][j]+=a[i][k] * b[k][j]
    for i in c:
        print( i )
print(mul([[1,2],[5,3]],[[2,3],[4,1]]))
