x = int(input("Enter the number"))
i=1
while True:
    if(x==i**4):
        print("True")
        break

    elif(i**4>x):
        print("False")
        break
    i+=1

      