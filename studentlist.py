name=input("enter the name of the student: ")
regno=input("enter the register number")
sub = int(input("Enter number of the subjects: "))
lis = []
summar = 0
for i in range(sub):
    lis.append(float(input(f"Enter marks of subject {i}: ")))
    summar += sum(marks)
print("student name ",name)
print("register number ",regno)
print("List of marks:", lis)
print(" sum of all marks:", summar)
avg=summar/5
print("Avg is ",avg)
