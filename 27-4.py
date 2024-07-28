def inter(set1,set2):
 intersection = set1 & set2
 result = list(intersection)
 return result
print(inter({1,2,2,4},{2,3}))
print(inter({1,9,8,7,9},{2,9,8}))
