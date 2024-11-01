print("-----------------------Welcome to the Calculator-----------------------")
print("-----------------------------------------------------------------------")
running = True

while running:
    n1 = float(input("Insert your first number: "))
    n2 = float(input("Insert your second number: "))
  
    user_operator = input("1. Addition 2. Subtraction \n3. Multiplication 4. Division\nSelect the operator(1,2,3,4): ")
    operator = {1:'Addition', 2: 'Subtraction', 3: 'Multiplication', 4:'Division'}
   
    print("-----------------------------------------------------------------------")

    if user_operator == "1": #Takes the keys from the dictionary
        r = (n1+n2) #Formula
        print(f"The addition of {n1}+{n2} = {r:.2f}")

    elif user_operator == "2": 
        r = (n1-n2)
        print(f"The subtraction of {n1}-{n2} = {r:.2f}")

    elif user_operator == "3":
        r = (n1*n2)
        print(f"The multiplication of {n1}*{n2} = {r:.2f}")


    elif user_operator == "4":
        r = (n1/n2)
        print(f"The division of {n1}/{n2} = {r:.2f}")

    if not input("Calculate again?(y/n): ") == "y": #Checks if the user wants to use the calculator again
        running = False

print("Thanks for using the calculator~")
