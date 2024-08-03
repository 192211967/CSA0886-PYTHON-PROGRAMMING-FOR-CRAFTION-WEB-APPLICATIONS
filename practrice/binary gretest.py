a = input("enter a binary number a: ")
b = input("enter a binary number b : ")
c = input("enter a binary number c: ")
p=int(a,2)
q=int(b,2)
r=int(c,2)
print(p,q,r)
if(p>q and p>r):
    print(a," is greater")
elif(q>p and q>r):
    print(b," is greater")
elif(r>p and r>q):
    print(c," is greater")
else:
    print("Invalid input")