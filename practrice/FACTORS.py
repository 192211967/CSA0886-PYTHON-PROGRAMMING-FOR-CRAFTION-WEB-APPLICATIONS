n = int(input('Enter a number: '))
N = int(input('Enter  to check Nth values: '))
lis=[]
c=0
for i in range(1,n+1):
    if (n % i == 0):
        c = c + 1
        lis.append(i)
print(N,"th  FACTOR IS ",lis[N-1])
print("NO OF FACTORS = ",c)



