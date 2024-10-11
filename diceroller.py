import random

dice_art = {
    1: ["┌─────────┐",
        "|         |",
        "|    ●    |",
        "|         |",
        "└─────────┘"],
    2: ["┌─────────┐",
        "|  ●      |",
        "|         |",
        "|      ●  |",
        "└─────────┘"],
    3: ["┌─────────┐",
        "|  ●      |",
        "|    ●    |",
        "|      ●  |",
        "└─────────┘"],
    4: ["┌─────────┐",
        "|  ●   ●  |",
        "|         |",
        "|  ●   ●  |",
        "└─────────┘"],
    5: ["┌─────────┐",
        "|  ●   ●  |",
        "|    ●    |",
        "|  ●   ●  |",
        "└─────────┘"],
    6: ["┌─────────┐",
        "|  ●   ●  |",
        "|  ●   ●  |",
        "|  ●   ●  |",
        "└─────────┘"],
}

num_of_dice = int(input("How many dice: "))

dice = []
total = 0

for die in range(num_of_dice):
   roll = random.randint(1, 6)
   dice.append(roll)

for line in range(5):
   for die in dice:
      print(dice_art[die][line], end = "  ")
   print()

for die in dice:
    total += die

print(f"\nTotal: {total}")
