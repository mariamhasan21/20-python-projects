food = []
price = []
total = 0
while True:
    foods = input("What foods would you like: ")
    if foods.lower() == "q":
        break
    else:
        prices = int(input("The price of the food: $"))
        food.append(foods)
        price.append(prices)

print("_________Your cart_________")

for foods in food:
    print(foods,end ="\n")

for prices in price: 
    total += prices


print(f"The total amount is ${total}")
