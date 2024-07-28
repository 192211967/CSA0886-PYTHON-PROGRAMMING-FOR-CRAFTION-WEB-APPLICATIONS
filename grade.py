def grade(maths,java,python,cloud):
 avg=(maths+python+java+cloud)/4
 print("Avarage of the student is ",avg)
 if(avg>90):
    print("S grade")
 elif(avg>80):
    print("A grade")
 elif(avg>70):
    print("B grade")
 elif(avg>60):
    print("C grade")
 elif(avg>50):
    print("D grade")
 elif(avg>40):
    print("F grade")
 else:
    print("invalid")
print(grade(100,97,99,100))    
