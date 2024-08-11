def sq(a,b):
    lis=[]
    for i in range(a,b+1):
        sqr=i*i
        if(sqr<=b+1):
           lis.append(sqr)
    print(lis)
sq(1,40)
