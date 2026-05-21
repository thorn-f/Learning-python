import random

def get_pick():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_user_pick():
    while True:
        user_input = input("Rock, paper, scissors? ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

def determine_winner(user_pick, computer_pick):
    if user_pick == computer_pick:
        return "It's a tie!"
    elif (user_pick == "rock" and computer_pick == "scissors") or \
         (user_pick == "paper" and computer_pick == "rock") or \
         (user_pick == "scissors" and computer_pick == "paper"):
        return "You win!"
    else:
        return "Computer wins!"