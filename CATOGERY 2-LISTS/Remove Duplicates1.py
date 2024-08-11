def rem(N):
    lis=[]
    res=[]
    for i in range(0,N):
        num=int(input(f"Enter the Element {i+1}: "))
        lis.append(num)
    print(lis)
    for i in lis:
        if(i not in res):
            res.append(i)
    print(res)
rem(7)

