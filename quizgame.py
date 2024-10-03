ques = ("What is the basic unit of life?: ", "What is the chemical formula for water?: ",
"What is the force of gravity between two objects?: ")
options = (
    ("A. Cell", "B. Organ", "C. Molecule"),
    ("A. H2O", "B. CO2", "C. NaCl"),
    ("A. Mass", "B. Weight", "C. Force")
)
answers = ("C", "A", "C")
guesses = []
score = 0
que_num = 0

for que in ques:
    print("----------------------")
    print(que)
    for option in options[que_num]:
        print(option)
    guess = input("Enter your guess (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[que_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[que_num]} is the correct answer!")
    que_num += 1

print("---------------")
print("     Result    ")
print("---------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(ques) * 100)
print(f"Your score is {score}%")
