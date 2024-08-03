a=[[True,False],[False,True]]
b=[[True,False],[False,True]]
c=[[False,False],[False,False]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            c[i][j]=c[i][j] or a[i][k] and b[k][j]
for i in c:
    print(c)
