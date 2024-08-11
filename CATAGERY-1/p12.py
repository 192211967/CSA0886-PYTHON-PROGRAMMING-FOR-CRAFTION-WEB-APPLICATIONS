n=6
for i in range(n,0,-1):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()