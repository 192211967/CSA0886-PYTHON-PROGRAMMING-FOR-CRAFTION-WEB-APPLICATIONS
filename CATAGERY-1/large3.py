a=int(input("ENTER VALUE OF A "))
b=int(input("ENTER VALUE OF B"))
c=int(input("ENTER VALUE OF C"))
if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(b,"is greater")
elif(c>a and c>b):
    print(c,"is greater")
else:
    print("INVALID")