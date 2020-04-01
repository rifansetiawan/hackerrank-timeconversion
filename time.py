from datetime import datetime
import time

timeinputan = input()
timetimetime = datetime.strptime(timeinputan,"%I:%M:%S%p")
time_24_hours = datetime.strftime(timetimetime,"%H:%M:%S") 
print(time_24_hours)