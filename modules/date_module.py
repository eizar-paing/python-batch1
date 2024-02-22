from datetime import date
import datetime

# get current date
today = datetime.date.today()
print(today)
# print(dir(datetime.date))

# get current date and time
current = datetime.datetime.now()
print(current.year)
print(current.strftime("%A"))

# specific date
specific_date = datetime.datetime(2021, 10, 5, 15, 30, 45)
print(specific_date)
format_date = specific_date.strftime("%Y %B %d")
print(format_date)
print(specific_date)

print(type(format_date))
print(type(specific_date))


