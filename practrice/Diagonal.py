def diagonal(a):
    ele=[]
    sum = 0
    for i in range(len(a)):
            if(a[i][i]):
                sum=sum+a[i][i]
                ele.append(a[i][i])
    print("Sum of diagonal is",sum)
    for i in ele:
        print(i)
diagonal([[1,2,3],[4,5,6],[7,8,9]])