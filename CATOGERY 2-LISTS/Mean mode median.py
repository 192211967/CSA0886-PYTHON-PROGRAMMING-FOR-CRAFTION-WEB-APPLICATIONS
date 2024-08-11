import statistics as sol
def stat(lis):
    mean1=sol.mean(lis)
    medi1=sol.median(lis)
    mode1=sol.mode(lis)
    print("mean is ",mean1)
    print("median is ",medi1)
    print("mode is ",mode1)
stat([1,2,3,4,1])