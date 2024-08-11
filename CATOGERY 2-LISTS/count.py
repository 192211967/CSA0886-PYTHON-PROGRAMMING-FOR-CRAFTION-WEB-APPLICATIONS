def freq(lis):
    res=[]
    lis1=set(lis)
    for i in lis1:
        for j in lis:
            c=lis.count(i)
        res.append((i,c))
    print(res)
freq([1, 1, 2, 2, 2, 3, 3, 3,4, 4, 5])
