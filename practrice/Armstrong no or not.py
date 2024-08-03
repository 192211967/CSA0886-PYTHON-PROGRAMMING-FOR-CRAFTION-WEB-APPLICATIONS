def is_armstrong(n):
    sum=0
    temp=n
    while(n!=0):
        rem=n%10
        sum=rem**3+sum
        n=n//10
    if(sum==temp):
        return True
    else:
        return False
print(is_armstrong(152))
