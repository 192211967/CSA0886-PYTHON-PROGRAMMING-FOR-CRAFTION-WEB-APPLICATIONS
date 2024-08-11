def spir(a):
    rows=len(a)
    cols=len(a[0])
    dir=1
    r=0
    c=0
    res=[]
    while rows>0 and cols>0:
        for i in range(cols):
            c+=dir
        res.append(a[r][c])
        rows-=1
        for i in range(rows):
            r+=dir
        res.append(a[r][c])
        cols-=1
        dir*=-1
    print(res)
spir([[1,2,3,4,5,6,7,8,9]])
