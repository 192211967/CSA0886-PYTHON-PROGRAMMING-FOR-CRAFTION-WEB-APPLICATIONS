def rem(lis,N):
    for i in range(len(lis)-1):
        lis.pop(N)
        print(lis)
        print(len(lis))
rem([3,2,2,3],3)