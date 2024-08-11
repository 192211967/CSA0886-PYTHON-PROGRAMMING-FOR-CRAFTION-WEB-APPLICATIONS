N=int(input("Enter the Limit of Number to be Entered: "))
lis=[]
sq=[]
sumod=0
sumev=0
for i in range(N):
    n=int(input(f"Enter the element {i+1}: "))
    lis.append(n)
print(lis)
for i in lis:
    if i%2==1:
       sumod+=i**2
    if(i%2==0):
        sumev+=i**2
sq.append(sumod)
sq.append(sumev)
print(sq)

