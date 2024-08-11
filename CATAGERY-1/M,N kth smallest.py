def kthSmallest(m,n,k):
    res=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            res.append(i*j)
    print(res)
    sorted(res)
    print(res)
    print(res[k-1])
kthSmallest(3,3,8)
