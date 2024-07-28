a=int(input("Enter the number: "))
for i in range(2,a+1):
    c=0
    for j in range(2,i+1):
        if(i%j==0):
            c+=1
    if(c==1):
        print(i)
