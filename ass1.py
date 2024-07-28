def Pow3(x):
 i=1
while True:
    if(x==i**3):
        return True
        break

    elif(i**3>x):
        return False
        break
    i+=1
print(Pow3(25))
print(Pow3(27))


      