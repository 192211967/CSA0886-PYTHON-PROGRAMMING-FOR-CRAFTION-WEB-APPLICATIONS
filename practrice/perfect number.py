def perfect(n):
    c=0
    sum=0
    for i in range(1,n):
        if n%i==0:
            c=c+1
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
print(perfect(28))