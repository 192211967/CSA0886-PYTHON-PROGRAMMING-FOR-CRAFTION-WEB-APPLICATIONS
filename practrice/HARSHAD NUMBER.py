def harshad(n):
    sum=0
    org=n
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    if(org%sum==0):
        return True
    else:
        return False
print(harshad(12))