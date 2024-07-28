n1=int(0)
n2=int(1)
ran=int(input("enter the range: "))
print(n2)
for i in range(2,ran+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
