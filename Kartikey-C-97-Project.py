import random

print('Number Guessing Game\nGuess a number between 1 and 9.')

number = random.randint(1, 9)
chances = 0

while chances < 3:
    guess = int(input('Enter your guess:- '))
    chances = chances+1
    if(number == guess):
        print('CONGRATULATIONS YOU WON!!!')
        exit()
    elif((number > guess) and (chances < 3)):
        text = 'Your guess fell short.Try guessing a number bigger than {}'
        print(text.format(guess))
    elif((number < guess) and (chances < 3)):
        text = 'You guessed a larger number.Try guessing a number smaller than {}'
        print(text.format(guess))

if not chances < 3:
    text = 'You Lose, the number was {}'
    print(text.format(number))