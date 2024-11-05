#Count Down Timer
import time
import os

def countdown_timer():
    try:
        my_time = int(input("Enter the timer (in seconds): "))
        if my_time < 0:
            print("Please enter a positive number")

        for x in range(my_time, 0, -1): #-1 jumps to the current time's previous one
            seconds = x % 60 #gives the remainder seconds that don't make up a full minute
            minutes = (x // 60) % 60
            hours = x // 3600 #3600 seconds per hour
            os.system('cls' if os.name == 'nt' else 'clear')
            # 'nt' is used in Windows for time known as 'New Technology'
            # If under the os system, the os name is 'nt' (for Windows), it will clear the
            # screen and show the timer in one line making the timer pleasing to eyes
            # Else is used to show the same thing for Linux and Mac OS 
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1) #The statement will execute with an interval of 1 second

        print("🎉 Yippee! Time's up! 🎉")
    except ValueError:
        print("Please enter a valid number.")

countdown_timer()
