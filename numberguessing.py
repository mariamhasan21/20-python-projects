import random
lowest = 1
highest = 100
answer = random.randint(lowest, highest)
guesses = 0

while True:
    guess = input("Guess the number: ")
    try:
        if guess.isdigit():
            guess = int(guess)
            guesses += 1

        if guess < lowest or guess > highest:
            print("Guess is out of range")
            print(f"Please select a number between {lowest} to {highest}")
        elif guess > answer:
            print("Too high! Check again")
        elif guess < answer:
            print("Too low! Check again")
        else:
            print("Correct!")
            print(f"Number of guesses: {guesses} times")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
