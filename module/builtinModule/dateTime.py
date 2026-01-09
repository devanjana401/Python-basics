from datetime import date, datetime
print(date.today())
print(datetime.now())

today = date.today()
print("Today's Date:", today) #Only Current Date

time_now = datetime.now().time()
print("Current Time:", time_now)#Only Current Time
#Creating a Specific Date or Time
my_birthday = date(1995, 12, 15)
print("My Birthday:", my_birthday)
meeting = datetime(2025, 11, 5, 14, 30)
print("Meeting Time:", meeting)

# Accessing Individual Components
now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

#Working with Time Differences (timedelta)
from datetime import datetime, timedelta
today = datetime.now()
next_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)
print("Today:", today)
print("Next Week:", next_week)
print("Yesterday:", yesterday)

#Find Difference Between Two Dates
d1 = date(2025, 11, 3)
d2 = date(2025, 12, 25)
difference = d2 - d1
print("Days left for Christmas:", difference.days)
#Formatting Dates and Times
now = datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted DateTime:", formatted)

#Converting String to Date (strptime)
from datetime import datetime
date_string = "2025-10-30 15:30:00"
converted = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Converted:", converted)

# Example – Countdown Timer (Simple)
from datetime import datetime
future = datetime(2025, 12, 31, 23, 59, 59)
now = datetime.now()
remaining = future - now
print("Time left until New Year:", remaining)

# Example – Check Expiry Date
from datetime import date
expiry_date = date(2025, 11, 15)
today = date.today()
if today > expiry_date:
    print("Expired")
else:
    print("Still Valid")

    