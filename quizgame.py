# Quiz game
# This program asks the users questions, and at the end of the program, it shows the answers and guesses and gives an accumulative score

ques = ("What is the basic unit of life?: ", "What is the chemical formula for water?: ",
"What is the force of gravity between two objects?: ")
options = (
    ("A. Cell", "B. Organ", "C. Molecule"),
    ("A. H2O", "B. CO2", "C. NaCl"),
    ("A. Mass", "B. Weight", "C. Force")
)

answers = ("C", "A", "C")
guesses = [] #Every guess given by the user will be appended here
score = 0 
que_num = 0


for que in ques:
    print("----------------------")
    print(que)
    for option in options[que_num]: #It will print 1, 2, 3 with each question
        print(option)
        
    guess = input("Enter your guess (A, B, C): ").upper() #Used upper in case user uses lowercase
    guesses.append(guess)
    
    if guess == answers[que_num]: #in this it will check against the guesses against answers one by one
        score += 1
        print("Correct!")
        
    else:
        print("Incorrect!")
        print(f"{answers[que_num]} is the correct answer!")
    que_num += 1

print("---------------")
print("     Result    ")
print("---------------")

print("Answers: ", end="") 
for answer in answers: #will show the answers in the same line
    print(answer, end = " ")
print()

print("guesses: ", end="")
for guess in guesses: #will show the guesses in the same line
    print(guess, end = " ")
print()

score = int(score / len(ques) * 100)
print(f"Your score is {score}%")
