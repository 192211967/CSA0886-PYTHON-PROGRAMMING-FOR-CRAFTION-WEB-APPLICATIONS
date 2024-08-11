def dup(lis):
    rem=[]
    for i in lis:
        if i not in rem and lis.count(i)==1:
            rem.append(i)
    print(rem)
dup([0,0,1,1,1,2,2,3,3,4,5])