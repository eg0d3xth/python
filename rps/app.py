import random

r = random
t = ["rock", "paper", "scissors"]

computer = t[r.randint(0, 2)]

player = False

while not player:
    player = input("\nChoose: ")
    if player == computer:
        print("\nTie!")
        player = False
        computer = t[r.randint(0, 2)]
    elif player == "rock":
        if computer == "paper":
            input("\nYou lose, computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
        elif computer == "scissors":
            input("\nYou win! Computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
    elif player == "paper":
        if computer == "rock":
            input("\nYou win! computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
        elif computer == "scissors":
            input("\nYou loose, computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
    elif player == "scissors":
        if computer == "rock":
            input("\nYou lose, computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
        elif computer == "paper":
            input("\nYou win! Computer was " + computer)
            player = False
            computer = t[r.randint(0, 2)]
    else:
        print("\nChoose: rock, paper or scissors")
        player = False
        computer = t[r.randint(0, 2)]