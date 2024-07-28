def inter(set1,set2):
 print(set1)
 intersection_set = set1 & set2
 result = list(intersection_set)
 return result
print(inter({1,2,3,4},{2,3}))