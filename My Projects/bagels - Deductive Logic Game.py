"""
Derived from - The Big Book of Small Python Projects by Al Sweigart
This is a game where you guess a number based off of various clues provided
"""

import random

NUM_DIGITS = 3  # Number of digits for the secret number
MAX_GUESSES = 10  # Number of guesses a player can make


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
with modifcations by Secho.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Bruh So Close One digit is correct but in the wrong position.
  Awwww Yeah    One digit is correct and in the right position.
  Big Oof       One digit is not in the number at all.

Normal Mode Example:
    if the secret number was 347 and your guess was 843, the
clues would be -
    Big Oof
    Awww Yeah
    Bruh So Close

Hard Mode example:
    if the secret number was 347 and your guess was 843, the
clues would be-
    Awww Yeah
    Big Oof 
    Bruh So Close'''.format(NUM_DIGITS))

    while True:
        mode = input("\nWould you like to play Normal or Hard mode?(N/H)").lower()
        if mode.startswith('n'):
            mode = 0
        elif mode.startswith('h'):
            mode = 1

        # This stores the number that the player needs to guess
        secretNumber = getSecretNumber()

        print("Okay, you have {} guesses to guess what number im thinking of ".format(MAX_GUESSES))

        guesses_made = 1
        guess = ''

        while guesses_made <= MAX_GUESSES and guess != secretNumber:
            guess = ''
            # look for valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('\nGuess #{}'.format(guesses_made))
                guess = input("Your Guess:")

                clues = getClues(guess, secretNumber, mode)
                print(clues)
                guesses_made += 1

                if guess == secretNumber:
                    break  # number is correct, so stop guessing even if it's before the max number of guesses
                if guesses_made > MAX_GUESSES:
                    print('You ran out of guesses >:(')
                    print('I was thinking of {}'.format(secretNumber))
                    break

        # Ask if player wants to go again
        print("\nWant to give it another go?(Y/N)")
        if not input("> ").lower().startswith('y'):
            break
    print("~Thanks for playing~")


def getSecretNumber():
    numbers = list('0123456789')  # Alternative constructor to square brackets []
    random.shuffle(numbers)

    # Get NUM_DIGITS places of list for the secretNumber
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNumber, hardmode):
    # Return words that indicate if a digit is correct or incorrect
    if guess == secretNumber:
        return 'Congrats~ You figured it out \\(^.^)/'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append("Awww Yeah")
        elif guess[i] in secretNumber:
            clues.append("Bruh so Close")
        elif guess[i] not in secretNumber:
            clues.append("Big Oof")
    else:
        # Sort clues into alphabetical order to hide as much info as possible
        if hardmode == 1:
            clues.sort()

        return '\n'.join(clues)  # return clues as a string


if __name__ == '__main__':
    main()