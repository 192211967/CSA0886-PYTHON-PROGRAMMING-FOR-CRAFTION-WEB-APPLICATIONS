def middle(lis):
    n=len(lis)
    lis.pop(0)
    lis.pop(-1)
    mid=lis
    return mid
print(middle([1,2,3,4,5]))
print(middle([8,8,9,10,11,12,8,8]))