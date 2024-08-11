p=0
n=0
sumN=0
lis=[]
while True:
    ip=int(input("Enter the number: "))
    if(ip==-1):
        break
    lis.append(ip)
print(lis)
sumP=0
for i in lis:
    if(i<0):
        n=n+1
        sumN=sumN+i
    if (i > 0):
        p = p + 1
        sumP = sumP + i
    avgP = sumP / p
print("Positive Avg is ", round(avgP, 2))
avgN=sumN/n
print("Negitive Avg is ",round(avgN,2))
