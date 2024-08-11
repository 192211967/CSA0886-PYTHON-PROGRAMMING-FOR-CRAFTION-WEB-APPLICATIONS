import calendar as cal
def day1(date):
    day,month,year=(int(i) for i in date.split('/'))
    dayno=cal.weekday(year,month,day)
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"]
    return days[dayno]
print(day1("09/08/2024"))
print(day1("31/08/2019"))