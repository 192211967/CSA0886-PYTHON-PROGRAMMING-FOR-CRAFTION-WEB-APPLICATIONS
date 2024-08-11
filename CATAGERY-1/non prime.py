a=int(input("enter starting range: "))
b=int(input("enter ending range: "))
for i in range(a,b+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                print(i)
                break