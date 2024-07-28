
f1=open('aj.txt', 'r')
content1 = f1.read()
f2= open('ar.txt', 'r')
content2 = f2.read()
o= open('blank.txt', 'w')
o.write(content1)
o.write('\n')  # Add a newline to separate the contents of the two files
o.write(content2)
print(f"Content merged  successfully.")
o= open('blank.txt', 'r')
print(o.read())
