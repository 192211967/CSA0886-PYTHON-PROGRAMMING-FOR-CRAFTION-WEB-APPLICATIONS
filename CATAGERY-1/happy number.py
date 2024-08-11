def happy(n):
    sum=0
    org=n
    while(n!=0):
        rem=n%10
        sum=sum+rem**2
        n=n//10
    return sum
n=int(input("Enter a number: "))
res=n
while res!=1 and res!=4:
    res=happy(res)
if(res==1):
    print("HAPPY NUMBER")
else:
    print("NO HAPPY NUMBER")




