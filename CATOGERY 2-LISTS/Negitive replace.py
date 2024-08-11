def replace(lis):
    avg=sum(lis)/len(lis)
    avg=round(avg,2)
    lis.sort()
    for i in range(len(lis)):
        if(lis[i]<0):
            lis[i]=avg
    print(lis)
replace([9,0,4,5,-1,6])

