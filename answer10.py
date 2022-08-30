#printing current date and time
from datetime import datetime,date
TodaysDate=date.today()
now = datetime.now()
timecurrently = now.strftime("H:%M%p")
print(TodaysDate,"and",timecurrently)