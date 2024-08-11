lst = [1, 2, 3, 4, 4]
t = 4
list=[]
for num in lst:
    if num!=t:
        list.append(num)
print(list)

#2.
a=[1,1,2,3,4,5]
list=[]
merge=set(sorted(a))
list.append(merge)
print(list)

#3.
list=[1,2,3,4,5,5]
rem=[]
for i in list:
    if i not in rem:
        rem.append(i)
print(rem)
#4.
list=[1,2,3,4,5,5]
ele=5
lis=[]
for i in list:
    if i!=ele:
        lis.append(i)
print(lis)