import math as m
def GCD(a,b):
    gcd=m.gcd(a,b)
    print(f"GCD is  {gcd}")
def LCM(a,b):
    gcd=m.gcd(a,b)
    lcm=(a*b)//gcd
    print(f"LCM is  {lcm}")
print(GCD(16,20))
print(LCM(16,20))