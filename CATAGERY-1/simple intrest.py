# //Write a program using function to calculate the simple interest. Suppose the
# customer is a senior citizen. She is being offered 15 percent rate of interest; he is being
# offered 12 percent rate of interest for all other customers, the ROI is 10 percent.
# Sample Input:
# Enter the principal amount: 200000 Enter the no of years: 3
# Gender (m/f): m
# Is customer senior citizen (y/n): n Sample Output:
# Interest: 60000
P=int(input("enter principal amount: "))
gen=input("enter Gender(M/F): ")
sc=input("enter Senior citizen(Y/N): ")
N=int(input("enter number of years: "))
if(gen=="M" and sc=="Y"):
    SI=(P*N*12)/100
    print(f"Simple interest is {SI}")
elif(gen=="F" and sc=="Y"):
    SI = (P * N * 15) / 100
    print(f"Simple interest is {SI}")
else:
    SI = (P * N * 10) / 100
    print(f"Simple interest is {SI}")
