def leap_year(year):
    if((year%4==0) and (year%100!=0) or (year%400==0)):
        return "LEAP YEAR"
    else:
        return "NOT LEAP YEAR"
print(leap_year(2024))