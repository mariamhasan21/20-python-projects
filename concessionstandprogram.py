#This program allows users to select food items from a menu, add chosen items to a cart, and calculate the total cost of the order.
menu = { #Stored the menu list in a dictionary with their prices
    "potato":22,
    "pizza": 12,
    "chips": 5,
    "macoroni cheese": 30,
    "donuts": 5,
    "soda": 3,
    "lemonade":7,
    "popcorn":5,
}
cart = [] #at the initial state, the cart is empty
total = 0 #total is also empty since no food is added
print("------------MENU------------")

for key, value in menu.items(): #for loop counts all of the food items from the menu dictionary
    print(f"{key:20}: ${value:.2f}") #20 for {key:20} is used for space

print("----------------------------")

while True:
    food = input("Enter the food you want to add to your cart (Press 'c' to see your final order) \nFood Name: ").strip().lower() 
    if food == "c": #condition to end the program
        break
    elif menu.get(food) is not None: #not None = negative+negative = positive.
        #Menu dictionary is checking if it's food items matches with the users food items 
        cart.append(food) #if the condition is true, the user's food items are added to the cart
        
        print(f"Added {food.capitalize()} to your cart.")
    
    else:
        print("Oopsie the food is not available on menu!") 
        #When the food is not to be found on the menu dictionary

print("-----------YOUR ORDER---------")

for food in cart:
    total += menu.get(food) #fetched the value of the menu dictionary since total was already an integer
    print(food, end = " ")

print(f"\nYour total is ${total:.2f}")
