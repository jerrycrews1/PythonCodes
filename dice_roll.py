from random import randint


def roll_dice():
    completed = False
    while not completed:
        try:
            sides = int(input("How many sides to your die? "))
            dice = int(input("How many dice would you like to roll? "))
            if sides > 1 and dice >= 1:
                break
            else:
                raise TypeError
        except (TypeError, ValueError):
            print("Oops, something went wrong.  Please try again")
            continue
    random_number = randint(1, sides)
    total = 0
    for i in range(dice):
        random_number = randint(1, sides)
        total += random_number
        print(f"Die {i + 1}: {random_number}")
    print(f"Total: {total}")


roll_dice()
