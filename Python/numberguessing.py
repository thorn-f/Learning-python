import random

def get_guess():
    return int(input("Guess a number between 1 and 10:"))

def check_guess(secret, guess):
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")

secret_number = random.randint(1, 10)
guessed_correctly = False

while not guessed_correctly:
    guess = get_guess()
    check_guess(secret_number, guess)
    if guess == secret_number:
        guessed_correctly = True
        