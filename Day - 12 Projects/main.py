# Number Guessing game in python.

import random


def fun(life, number):
    run = True
    while life and run:
        print(f"You have {life} attempts remaining to guess the number.")
        num = int(input("make a guess:"))
        if number > num:
            print("Too low.")
        elif number < num:
            print("Too High.")
        else:
            run = False
        print(f"You Guessed the Number.The Number is {num}")
        life -= 1
    if life == 0:
        print("You Lose.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
level = input("Choose a level: 'easy' or 'hard':")
if level == 'easy':
    fun(10, number)
elif level == 'hard':
    fun(5, number)
