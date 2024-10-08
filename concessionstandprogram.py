menu = {
    "potato":22,
    "pizza":10,
    "popcorn":5,
    "chips":8,
    "soda": 3,
    "lemonade":7,
    "donuts":5
}
cart = []
total = 0
print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------")

while True:
    food = input("Enter the food (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Oopsie the food is not available on menu!")
print("--------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end =" ")

print()
print(f"Your total is ${total:.2f}")
