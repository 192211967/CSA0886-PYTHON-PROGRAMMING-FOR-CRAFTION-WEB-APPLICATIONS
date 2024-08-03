def rowSum(a):
    for i in range(len(a)):
        sum=0
        for j in range(len(a[0])):
            sum=sum+a[i][j]
        print(f"{i+1}st row sum is {sum} ")
rowSum([[1,2,3],[4,5,6],[7,8,9]])
def colSum(a):
    for i in range(len(a)):
        sum=0
        for j in range(len(a[0])):
            sum=sum+a[j][i]
        print(f"{i+1}st column sum is {sum} ")
colSum([[1,2,3],[4,5,6],[7,8,9]])
