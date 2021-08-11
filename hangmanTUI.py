#!/usr/bin/env python3
from random import randint
import os
import sys

def clear():
    # Clears the terminal/command prompt when called
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def getWord():
    f = open('wordList.txt', 'r')

    with open('wordList.txt', 'r') as f:
        words = [line.strip() for line in f]

    return words[randint(0, len(words))]

def drawBoard(numb):
    if numb == 0:
        print('''
  ________
  |       |
          |
          |
          |
          |       
        -----''')
    elif numb == 1:
        print('''
  ________
  |       |
  O       |
          |
          |
          |       
        -----''')
    elif numb == 2:
        print('''
  ________
  |       |
  O       |
  |       |
          |
          |       
        -----''')
    elif numb == 3:
        print('''
  ________
  |       |
  O       |
  |-      |
          |
          |       
        -----''')
    if numb == 4:
        print('''
  ________
  |       |
  O       |
 -|-      |
          |
          |       
        -----''')
    if numb == 5:
        print('''
  ________
  |       |
  O       |
 -|-      |
 |        |
          |       
        -----''')
    if numb == 6:
        print('''
  ________
  |       |
  O       |
 -|-      |
 | |      |
          |       
        -----''')

def gameOver(result, word = ""):
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose! The correct word was " + word + ".")

def playAgain():
    userChoice = input("Would you like to play again? [Y/N] ")
    validYes = ["yes", "y", "YES", "Y"]
    validNo = ["no", "n", "N", "NO"]

    while userChoice not in validYes and userChoice not in validNo:
         userChoice = input(userChoice + " is not a valid option. Would you like to play again? [Y/N] ")

    if userChoice in validYes:
        gameLoop()
    elif userChoice in validNo:
        sys.exit()

def gameLoop():
    global guessedLetters
    guessedLetters = []
    life = 0
    userText = "Please enter your guess"
    word = getWord().upper()
    hiddenWord = ["_"] * len(word)
    guess = ""
    gameEnd = False
    valid = True

    while gameEnd != True:
        clear()
        valid = True
        drawBoard(life)

        for i in hiddenWord:
            print(i, end="")

        #print("\n" + word)
        print("\nGuessed Letters: ", end="")
        for let in guessedLetters:
            print(let, end=" ")
        print("")
        
        # Check for win
        if "_" not in hiddenWord:
            gameOver("win")
            break

        # Check for loss
        if life >= 6:
            gameOver("lose", word)
            break

        print(userText)
        guess = input().upper()[0]
        
        # Check that guess is a letter
        if guess.isalpha() == False:
            userText = "That is not a letter. Please guess again."
            valid = False

        # Check to make sure the letter hasn't been guessed already
        if guess in guessedLetters:
            userText = "You already guessed that letter. Please guess again."
            valid = False

        if valid:
            guessedLetters.append(guess)
            userText = "Please enter your guess"
            if guess not in word:
                life += 1
            for char in range(0, len(word)):
                if guess == word[char]:
                    hiddenWord[char] = guess

    playAgain()

if __name__ == "__main__":
    gameLoop()