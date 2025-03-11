import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
time1 = int(time.strftime('%H'))
time2 = int(time.strftime('%M'))
time3 = int(time.strftime('%S'))
if(time1<=11 and time1>0):
    print("Good Morning")
elif (time1>12 and time1<18):
  print("Good Afternoon sir")
  
else:
  print("Good Evening sir")
  