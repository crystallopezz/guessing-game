"""A number-guessing game."""
import random
print("Hello player!")
name = input("What is your name?")
random_number = random.randint(1, 100)
print("Can you guess what number I'm thinking of between 1-100?")
