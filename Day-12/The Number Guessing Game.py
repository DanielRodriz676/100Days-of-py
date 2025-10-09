from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    difficulty = 10
elif difficulty == 'hard':
    difficulty = 5

guess_num = random.choice(range(100))
for x in range(difficulty, 0, -1):
    print(f"You have {x} attempts remaining to guess the number")
    num = int(input("Make a guess: "))
    if num == guess_num:
        print(f"You got it! The answer was {guess_num}")
        break
    elif num > guess_num:
        print('Too high.')
    elif num < guess_num:
        print('Too low.')
    print('Guess again.')
print("You've run out of guesses, you lose.")