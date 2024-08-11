st=input("Enter a string: ")
let = 0
dig = 0
char='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
num='0123456789'
for i in range(len(st)):
    if st[i] in char:
        let=let+1
print("no of letters are ",let)
for i in range(len(st)):
    if st[i] in num:
       dig=dig+1
print("no of digits are ",dig)
