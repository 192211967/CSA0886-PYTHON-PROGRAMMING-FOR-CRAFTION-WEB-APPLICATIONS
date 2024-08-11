def find(lis):
    res=[]
    for i in lis:
        if lis.count(i)>1:
            res.append(i)
    res=set(res)
    res=list(res)
    print(res)
find([1,2,3,3,4])