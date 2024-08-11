def maxgus(T,E,L):
    max_=0
    curr=0
    for i in range(T):
        curr+=E[i]
        curr-=L[i]
        if(curr>max_):
            max_=curr
    print(max_)
maxgus(5,[6, 0, 5,4, 3],[1, 2, 1, 3, 4])