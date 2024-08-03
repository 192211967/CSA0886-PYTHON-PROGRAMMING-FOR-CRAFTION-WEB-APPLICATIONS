def Tech(n):
    m=str(n)
    a=m[:len(m)//2]
    b=m[len(m)//2:]
    c=int(a)+int(b)
    d=c**2
    if(d==n):
        return True
    else:
        return False
print(Tech(2025))