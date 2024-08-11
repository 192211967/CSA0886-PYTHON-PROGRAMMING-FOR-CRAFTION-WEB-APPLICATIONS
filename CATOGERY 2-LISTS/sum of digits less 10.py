def sumof(num):
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum+rem;
        num=num//10
        if(num==0 and sum>9):
            num=sum
            sum=0
    print("Sum is ",sum)
sumof(2999999999)
