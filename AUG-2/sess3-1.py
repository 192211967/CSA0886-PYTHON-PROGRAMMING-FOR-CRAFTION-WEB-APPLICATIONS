def cumsum(lis,n):
    rows=len(lis)
    sum=0
    for i in range(rows):
        if(i<=n):
              sum+=lis[i]
    return sum
print(cumsum([1,2,3,4],2))
