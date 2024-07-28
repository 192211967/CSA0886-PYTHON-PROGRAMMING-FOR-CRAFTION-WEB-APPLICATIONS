"""
Find the sum of all the positive numbers entered by the user.
NOTE: As soon as the user enters a negative number, stop taking in any further input from the user and
display the sum.
Test Case 1: Input: 3 4 5 -1
Output: 12
Test Case 2: Input: 2 4 6 -5
Output: 12
"""
sum=0
while True:
    a = int(input("Enter a number: "))
    if a<0:
        break
    sum+=a
print("Sum is ",sum)

    
      

      