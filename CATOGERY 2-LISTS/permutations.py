import itertools as sol
def per(lis):
    permut=list(sol.permutations(lis))
    print(permut)
per([1,1,3])