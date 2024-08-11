def factorial(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f
sum=0
N=int(input("Enter the limit of the factorial for adding : "))
for i in range(1,N+1):
    fac=factorial(i)
    div=fac//i
    sum=sum+div
print(sum)
