def is_power(a,b):
    if b<=1:
        return False  # b must be greater than 1 for powers to make sense
    while a>1:
        if a%b!=0:
            return False
        a=a//b
    return a == 1
print(is_power(27, 3))  # True, because 27 is 3^3
print(is_power(28, 7))  # False, because 28 is not a power of 3
