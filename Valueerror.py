try:
    ip=int(input("enter the value: "))
    print(ip)
except ValueError as e:
    print("An Error has Occured.",e)
