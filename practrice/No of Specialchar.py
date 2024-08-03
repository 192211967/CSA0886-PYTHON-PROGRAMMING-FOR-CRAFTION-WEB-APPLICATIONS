def count1(stri):
    sp="!@#$%^"
    c=0
    for i in range(len(stri)+1):
        if stri[i] in sp:
             c=c+1
    return c
print(count1("Iamavi!@#"))
