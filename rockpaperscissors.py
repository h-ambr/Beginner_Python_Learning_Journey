# Rock, Paper, Scissors game

import random
options = ("Rock", "Paper", "Scissors")
running = True

while running:
    player = None
    computer = random.choice(options).title()
    while player not in options:
        player = input("Enter a choice (rock, paper scissors): ").title()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    wins = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if player == computer:
        print("IT IS A TIE")
    elif wins[player] == computer:
        print("YOU WIN!!!!")
    else:
        print("YOU LOSE!!!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        break
print("Thanks for playing!")
