def findindex(lis,tar):
    res=[]
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]+lis[j]==tar):
                res.append((i+1,j+1))
    print(res)
findindex([2,3,4,4],6)

