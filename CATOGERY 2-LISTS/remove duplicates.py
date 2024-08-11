def remove1(lis):
    rem=[]
    for i in lis:
        if i not in rem and lis.count(i)==1:
            rem.append(i)
    print(rem)
remove1([1,2,2,3,4,4,5,5,7])