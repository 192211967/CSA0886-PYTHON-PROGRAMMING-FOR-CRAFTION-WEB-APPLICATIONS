import math as sol
num1=int(input("Enter the first num: "))
num2=int(input("Enter the second num: " ))
gcd=sol.gcd(num1,num2)
lcm=num1*num2/gcd
print("The LCM is: ",lcm)
print("The GCD is ",gcd)

