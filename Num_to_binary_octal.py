n=float(input("Enter the number "))
b=float(0)
i=1
while n!=0:
    rem=n%2
    b=b+rem*i
    n=n/2
    i=i*10
print(f"binary number is {b}")