def is_duplicates(lis):
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if (lis[i]==lis[j]):
                return True
    return False
print(is_duplicates([1,2,2,3,4]))
print(is_duplicates([1,2,3,4,5]))