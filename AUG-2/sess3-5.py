def nested_sum(lis):
    rows=len(lis)
    sum=0
    cols=len(lis[0])
    for i in range(rows):
        for j in range(cols):
            sum+=lis[i][j]
    return sum
print(nested_sum([[1,2,3],[4,5,6],[7,8,9]]))
