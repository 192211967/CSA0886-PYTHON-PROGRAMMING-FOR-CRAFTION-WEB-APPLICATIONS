def is_sort(lis):
    for i in range(len(lis)-1):
        if (lis[i]>lis[i+1]):
            return False
    return True
print(is_sort([9,1,2,5,4,8]))
print(is_sort([3,1,2,4,5]))
print(is_sort([1,2,3,4,5]))