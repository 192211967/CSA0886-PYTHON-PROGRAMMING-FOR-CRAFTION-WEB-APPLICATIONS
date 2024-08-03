def chop(lis):
    lis.pop(0)
    lis.pop(-1)
    return lis
print(chop([1,1,2,3,4,5,6,7,8,8]))