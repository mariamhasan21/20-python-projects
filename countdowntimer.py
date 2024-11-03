#Count down timer
import time
my_time = int(input("Enter the timer: "))
for x in range(my_time, 0, -1): #-1 jumps to the current time's previous one
    seconds  = int(x%60) #gives the remainder seconds that don't make up a full minute
    minutes = int(x// 60) %60
    hours = int(x// 3600) #3600 seconds per hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Yippe, times up!")

