def palindrome(num):
    temp = num
    if num < 0:
        return False
    else:
        rev = 0
        while num != 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        return temp==rev
print(palindrome(121))  
print(palindrome(-121))

