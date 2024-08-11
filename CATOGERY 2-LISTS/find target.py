def finding(lis,t):
    res=[]
    for i in range(len(lis)):
        if(lis[i]==t):
            res.append(i)
    print(res)
finding([5,7,7,8,8,10],8)
