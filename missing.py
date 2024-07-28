def missing(lis):
 maxi = max(lis)
 out = set(range(1,maxi+1))-(set(lis))
 return out
print(missing([1,2,3,4,6]))
print(missing([1,2,4]))

