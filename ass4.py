x = int(input("Enter the number"))
i=1
while True:
    if(x==i**2):
        print("True")
        break

    elif(i**2>x):
        print("False")
        break
    i+=1

      