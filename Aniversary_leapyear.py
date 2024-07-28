year=int(input("enter the year "))
month=int(input("enter the month "))
day=int(input("enter the day "))
if year%4==0:
    print(f"The year is leap year! Animersary date is {day}/{month}/{year+1} ")
else:
    print(f"The year is  not leap year! Animersary date is {day}/{month}/{year-1} ")