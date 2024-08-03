def miss(lis):
    maxi=max(lis)
    miss=set(range(0,maxi+1))-set(lis)
    return miss
print(miss([1,2,3,4,7,8]))