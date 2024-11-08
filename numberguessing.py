#Number Guessing Program
# This program uses random function and lets the user choose a number to try and guess

import random
#Defining the range from 0 to 100
lowest = 1 
highest = 100
answer = random.randint(lowest, highest) #Randint gives a range to random numbers
guesses = 0 

#Using while loop to make sure the program runs till the user guesses the correct number
while True:
    try:
        guess = int(input("Enter the number: "))
        guesses += 1 #This will keep the record of the user trying to guess the correct numeber
        if answer == guess:
            print("Correct 🎉")
            print(f"Number of guesses: {guesses} times")
            break
        
        elif guess < 0:
            print("Number can't be negative")
        
        elif guess < lowest or guess > highest:
            print("Guess is out of range")
            print(f"Please select a number between {lowest} to {highest}")

        elif answer < guess:
            print("Too high")

        elif answer > guess:
            print("Too low")
        
        else:
            print("Correct!")
            print(f"Number of guesses: {guesses} times")
            break

    except ValueError: #Shows this message if user do not provide int input
        print("Invalid input")

    except Exception as e:
        print(f"An unexpected error occured {e}")
