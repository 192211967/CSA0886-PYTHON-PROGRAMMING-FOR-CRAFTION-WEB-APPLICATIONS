ip1=input("Enter a Binary number: ")
ip2=input("Enter a Binary number: ")
a=int(ip1,2)
b=int(ip2,2)
sum1=a+b
op=bin(sum1)[2:]
print("Addition is ",op)