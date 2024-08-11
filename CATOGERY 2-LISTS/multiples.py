#Write a python program to compute the sum of all the multiples of 3 and 5 below 200.
def multi(N):
    res=[]
    for i in range(1,N):
        if(i%3==0 and i%5==0):
            res.append(i)
    sum1=sum(res)
    print(sum1)
multi(200)
