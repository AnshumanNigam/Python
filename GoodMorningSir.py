# Creating a python program capable of greeting Good Morning ,Good Afternoon and Good Evening.
# Use Module to get the current time

import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if(timestamp>=0 and timestamp <12):
   print("Good Morning Sir!!! ")
elif(timestamp>=12 and timestamp<17):
   print("Good Afternoon Sir!!! ")
elif(timestamp>=17 and timestamp<0):
   print("Good Night Sir!!! ")