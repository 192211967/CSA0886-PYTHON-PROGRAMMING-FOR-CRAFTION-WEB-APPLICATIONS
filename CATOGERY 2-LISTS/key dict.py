import itertools as it
def combi(d):
    lis=list(d.values())
    comb=it.product(*lis)
    for i in comb:
        print(''.join(i))
combi(
    {
    'a':['a','b'],
    'b':['c','d']
    }
)