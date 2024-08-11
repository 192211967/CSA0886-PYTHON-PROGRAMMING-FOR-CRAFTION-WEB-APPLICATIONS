def bound(a):
    rows=len(a)
    cols=len(a[0])
    for i in range(rows):
        for j in range(cols):
            if(i==0):
                print(a[i][j],end=''),
            elif(i==rows-1):
                print(a[i][j],end=''),
            elif(j==0):
                print(a[i][j],end=''),
            elif(j==cols-1):
                print(a[i][j],end=''),
            else:
                print(""),
        print()
bound([[1,2,3],[4,5,6],[7,8,9]])
