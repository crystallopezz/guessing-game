"""A number-guessing game."""
import random
print("Hello player!")
name = input("What is your name?")
random_number = random.randint(1, 100)
tries = 0
current_guess = input("Can you guess what number I'm thinking of between 1-100?")
try: 
    current_guess = int(current_guess)
except: 
    current_guess = int(input("Please write a valid number between 1-100"))
if current_guess < 0 or current_guess > 101:
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