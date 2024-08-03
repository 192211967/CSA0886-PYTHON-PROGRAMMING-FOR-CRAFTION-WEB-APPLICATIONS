def pyrt1(limit):
  for i in range(1,limit+1):
     for j in range(i+1,limit+1):
        for k in range(j+1,limit+1):
            if((i**2)+(j**2)==(k**2)):
             print(i,j,k)
print(pyrt1(10))

