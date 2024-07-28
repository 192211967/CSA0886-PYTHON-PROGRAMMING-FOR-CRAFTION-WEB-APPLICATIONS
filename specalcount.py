def count(str):
    s=0
    schar='!@#$%^&*()_+'
    for i in str:
        if(i in schar):
            s=s+1
            print(i)
    print(f"special char are {s}")
print(count("hello! i @m avi"))