# #Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of
# [20,20,30,30] separately.
def prof(dif,p,w):
    ind=[]
    res=[]
    for i in range(len(dif)):
        for j in range(len(w)):
            if(dif[i]==w[j]):
                ind.append(i)
    print(ind)
    sum=0
    for i in range(len(ind)):
            sum=sum+(p[ind[i]]*2)
    print(sum)
prof([13,37,58],[4,90,96],[34,73,45])

