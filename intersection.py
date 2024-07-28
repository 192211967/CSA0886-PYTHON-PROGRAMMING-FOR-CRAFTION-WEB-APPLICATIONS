def inter(set1,set2):
 intersection_set = set1 & set2
 result = list(intersection_set)
 return result
print(inter({1,2,3,4},{2,3}))
print(inter({1,9,8,7,9},{2,9,8}))
