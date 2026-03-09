import random

opponent = random.choice([-1, 0, 1])

Mychoice = {"p": -1, "r": 0, "s": 1}
Computerchoice = {-1: "paper", 0: "rock", 1: "scissors"}

user = input("Enter the first letter of your choice (p/r/s): ").lower()

if user not in Mychoice:
    print("Invalid choice.")
    exit()

you = Mychoice[user]

print(f"You chose {Computerchoice[you]} and Computer chose {Computerchoice[opponent]}")


if you == opponent:
    print(" Draw ")
else:
    if you == 1 and opponent == -1:
        print(" You Win ")
    elif you == -1 and opponent == 1:
        print(" Computer Wins ")
    elif you == 0 and opponent == -1:
        print(" You Win ")
    elif you == -1 and opponent == 0:
        print(" Computer Wins ")
    elif you == 1 and opponent == 0:
        print(" You Win ")
    elif you == 0 and opponent == 1:
        print(" Computer Wins ")
