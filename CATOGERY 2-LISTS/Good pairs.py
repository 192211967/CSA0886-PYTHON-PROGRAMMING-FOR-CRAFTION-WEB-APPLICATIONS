def good(lis):
    c=0
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]==lis[j]):
                c=c+1
                print([(i,j)],end='')
                print()
    print("No of good pairs",c)
good([1,2,3,1,1,3])
