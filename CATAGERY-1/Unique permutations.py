import itertools as sol
def permut(str1):
    p=set(sol.permutations(str1))
    for P in p:
        print([''.join(P)])
permut("112")