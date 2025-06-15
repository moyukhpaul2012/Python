'''
------------ GAME RULES ------------

1. We will first ask the user if the user really wants to roll the dice

2. If entered value anything except y and n it will display as an invalid input

3. If entered value as y the program shows a dice value

4. If entered value as yn the program exits by bidding the user 'Thanks for playing'

'''
import random

while True:
    choice= input("Roll the dice? (yes (y)/no (n)): ").lower
    if choice == "y":
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        print(f"({dice1}, {dice2})")

    elif choice == "n":
        print("Thanks for playing!")
        break

    else:
        "Invalid Choice!"