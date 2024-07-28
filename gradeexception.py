try:
 maths=int(input("enter the marks in the mathamatics "))
 python=int(input("enter the marks in python "))
 java=int(input("enter the marks in java "))
 cpp=int(input("enter the marks in cpp "))
 cloud=int(input("enter the marks in cloud "))
 n=int(input("enter the no of subjects"))
 avg=(maths+python+java+clouds)/n
except NameError:
 print("error!check subject name  entered correctly")
else:
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
    print("invalid grade")
