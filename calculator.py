print("__________Welcome to the Calculator__________".center(50))
n1 = float(input("Hey insert your first number: "))
n2 = float(input("Hey insert your second number: "))
operator = input("Select the operator: '+ - * /': ")
if operator == "+":
    r = (n1+n2)
    print(r)
elif operator == "-":
    r = (n1-n2)
    print(r)
elif operator == "*":
    r = (n1*n2)
    print(r)

elif operator == "/":
    r = (n1/n2)
    print(r)
