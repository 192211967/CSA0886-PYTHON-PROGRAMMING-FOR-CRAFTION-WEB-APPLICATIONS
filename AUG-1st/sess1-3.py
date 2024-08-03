def eas(n):
    s = bin(n)[2:]
    print(s)
def sol(n):
    b=0
    i=1
    while (n != 0):
        rem=n%2
        b=b+i*rem
        n = n//2
        i = i*10
    print(b)
print(eas(42))
print(sol(42))

