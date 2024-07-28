"""
Print the Factorial of the given value.
Test Case 1: Input: n = 3
Output: 6
Test Case 2: Input: n = 5
Output: 120
"""
a=int(input("ip: "))
fact=int(1)
for i in range(1,a+1):
    fact=fact*i
print("factorial ",fact)