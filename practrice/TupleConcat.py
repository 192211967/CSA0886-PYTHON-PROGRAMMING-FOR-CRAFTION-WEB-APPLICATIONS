def con(tuple1,tuple2):
    concat=tuple1+tuple2
    ele = int(input("ENTER AN ELEMENT TO FIND INDEX: "))
    if ele in concat:
        ind=concat.index(ele)
        return ind,concat
    else:
        return "NO INDEX FOUND",concat
print(con((1,2,3),(4,5,6) ))
