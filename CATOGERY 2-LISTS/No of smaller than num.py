def small(lis):
    res=[]
    for i in range(len(lis)):
        c=0
        for j in range(len(lis)):
            if(lis[j]<lis[i] and i!=j):
                c=c+1
        res.append(c)
    print(res)
small([8,1,2,2,3])