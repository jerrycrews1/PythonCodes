from random import randint


def guessing_game():
    attempts = 1
    while True:
        try:
            upto = int(input("What range would you like? 1 - "))
            if upto >= 2:
                break
            else:
                raise TypeError
        except (TypeError, ValueError):
            print("You must enter a valid number greater than 1")
            continue

    random_number = randint(1, upto)

    while True:
        try:
            guess = int(input(f"Awesome, guess a number 1 - {upto}: "))
            if upto >= guess >= 1:
                break
            else:
                raise TypeError
        except (TypeError, ValueError):
            print(f"You must enter a valid number between 1 and {upto}")
            continue

    while guess != random_number:
        attempts += 1
        guess = int(input(f"Nope, try again.  Guess a number 1 - {upto}: "))
    if attempts == 1:
        return print(f"Wow, first try!!!")
    else:
        return print(f"Correct! It took you {attempts} attempts.")


guessing_game()
