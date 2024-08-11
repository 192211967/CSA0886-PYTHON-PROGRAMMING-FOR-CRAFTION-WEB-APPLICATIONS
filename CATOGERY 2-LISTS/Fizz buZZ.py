def div(n):
    res=[]
    for i in range(1,n+1):
         if(i%3==0 and i%5==0):
             res.append("FIZZ BUZZ")
         elif(i%3==0):
             res.append("FIZZ")
         elif(i%5==0):
             res.append("Buzz")
         else:
             res.append(f"{i}")
    print(res)
div(15)

