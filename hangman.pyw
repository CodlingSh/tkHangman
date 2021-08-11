#!/usr/bin/env python3

from random import randint
import tkinter as tk
from tkinter import messagebox
import sys
from tkinter.constants import DISABLED

def getWord():
    f = open('wordList.txt', 'r')

    with open('wordList.txt', 'r') as f:
        words = [line.strip() for line in f]

    return words[randint(0, len(words))]

def listToString(list):
    theString = ""

    for i in list:
        theString += i + " "

    return theString

def makeGuess(let):
    global word
    global life
    global gallow
    check = True

    if let not in word:
        life += 1
        gallow.grid_forget()
        gallow = tk.Label(root, image=imgList[life], background="#1c1c1c")
        gallow.place(x=215, y=10)
        check = False
        if life >= 6:
            showMessage("lose")

    if check == True:
        for i in range(0, len(word)):
            if let == word[i]:
                hiddenWord[i] = word[i]
                board.config(text = listToString(hiddenWord))
        if "_" not in hiddenWord:
            showMessage("win")

def showMessage(condition):
    global word
    if condition == "win":
        mBox = messagebox.askyesno("Congradulations!", "You win! \n\nWould you like to play again?")
    elif condition == "lose":
        mBox = messagebox.askyesno("Game Over!", "You lose! The correct word was " + word + "\n\nWould you like to play again?")

    if mBox == 1:
        board.destroy()
        gallow.destroy()
        for btn in btnList:
            btn.removeBtn()
        gameLoop()
    elif mBox == 0:
        sys.exit()

class GuessButton:
    def __init__(self, master, letter, xPlace, yPlace):
        self.letter = letter
        self.newButton = tk.Button(master, text=self.letter, width=6, height=3, font='bold', command=lambda: self.clicked(), background="#1c1c1c", foreground="#FFFFFF", bd=2, activebackground="#444444", activeforeground="#EEEEEE")
        self.newButton.place(x = xPlace, y = yPlace)

    # Destroy the guessButton when clicked
    def clicked(self):
        self.newButton.destroy()
        makeGuess(self.letter)

    # Destroy all the buttons if the user wants to play again.
    def removeBtn(self): 
        self.newButton.destroy()

def gameLoop():
    global hiddenWord, word, gallow, life, root, imgList, board, btnList
    word = getWord().upper()
    life = 0
    hiddenWord = ["_"] * len(word)
    
    gallow = tk.Label(root, image=img0, background="#1c1c1c")
    gallow.place(x=215, y=10)
    board = tk.Label(root, width = 20, height = 2, font=("Sans", 30), text=listToString(hiddenWord), background="#1c1c1c", foreground="#FFFFFF")
    board.place(x=95, y=205)

    a = GuessButton(root, "A", 38, 277+25)    
    b = GuessButton(root, "B", 103, 277+25)
    c = GuessButton(root, "C", 168, 277+25)
    d = GuessButton(root, "D", 233, 277+25)
    e = GuessButton(root, "E", 298, 277+25)
    f = GuessButton(root, "F", 363, 277+25)
    g = GuessButton(root, "G", 428, 277+25)
    h = GuessButton(root, "H", 493, 277+25)
    i = GuessButton(root, "I", 558, 277+25)
    j = GuessButton(root, "J", 38, 346+25)
    k = GuessButton(root, "K", 103, 346+25)
    l = GuessButton(root, "L", 168, 346+25)
    m = GuessButton(root, "M", 233, 346+25)
    n = GuessButton(root, "N", 298, 346+25)
    o = GuessButton(root, "O", 363, 346+25)
    p = GuessButton(root, "P", 428, 346+25)
    q = GuessButton(root, "Q", 493, 346+25)
    r = GuessButton(root, "R", 558, 346+25)
    s = GuessButton(root, "S", 70, 415+25)
    t = GuessButton(root, "T", 135, 415+25)
    u = GuessButton(root, "U", 200, 415+25)
    v = GuessButton(root, "V", 265, 415+25)
    w = GuessButton(root, "W", 330, 415+25)
    x = GuessButton(root, "X", 395, 415+25)
    y = GuessButton(root, "Y", 460, 415+25)
    z = GuessButton(root, "Z", 525, 415+25)
    btnList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hang Man")
    root.iconbitmap('mainIcon.ico')
    root.geometry("660x520")
    root.resizable(False, False)
    root.configure(background='#1c1c1c')

    # Load the images
    img0 = tk.PhotoImage(file="life/0.png")
    img1 = tk.PhotoImage(file="life/1.png")
    img2 = tk.PhotoImage(file="life/2.png")
    img3 = tk.PhotoImage(file="life/3.png")
    img4 = tk.PhotoImage(file="life/4.png")
    img5 = tk.PhotoImage(file="life/5.png")
    img6 = tk.PhotoImage(file="life/6.png")
    imgList = [img0, img1, img2, img3, img4, img5, img6]

    gameLoop()