"""A number-guessing game."""
import random
print("Hello player!")
name = input("What is your name?")
random_number = random.randint(1, 100)
first_guess = int(input("Can you guess what number I'm thinking of between 1-100?"))
current_guess = first_guess
def guessing_game (current_guess, random_number):
    tries = 0
    if current_guess not in range(1,100):
        current_guess = int(input("Not in range, please try again"))
    while current_guess != random_number:
        tries = tries+1
        if current_guess > random_number:
            current_guess = int(input("Too high"))
        if current_guess < random_number:
            current_guess = int(input("Too low"))
    else: 
        tries = tries+1
        print("Congrats, you guessed it in ",tries," tries!")
try:
    guessing_game(current_guess, random_number)
except: 
    current_guess = int(input("Not a valid number, try again"))
