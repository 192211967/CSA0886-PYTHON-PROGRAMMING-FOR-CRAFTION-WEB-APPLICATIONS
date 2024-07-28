a=int(input("enter the num1"))
b=int(input("enter the number 2"))
try:
    c=a/b
except ZeroDivisionError:
    print("error! denominator should not be zero ")
else:
    print(c)

