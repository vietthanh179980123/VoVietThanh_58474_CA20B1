"""
    Name: Võ Viết Thanh
    Date:30/10/2021
    File: dicedemo.py
    Pops up a window that allows the user to roll the dice.
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from die import Die

class DiceDemo(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self, title = "Dice Demo")
            self.setSize(220, 200)
            self.die1 = Die()
            self.die2 = Die()
            self.dieLabel1 = self.addLabel("", row = 0, column = 0, sticky = "NSEW")
            self.dieLabel2 = self.addLabel("", row = 0, column = 1, sticky = "NSEW", columnspan = 2)
            self.stateLabel = self.addLabel("", row = 1, column = 0, sticky = "NSEW", columnspan = 2)
            self.addButton(row = 2,column = 0, text = "Roll",command = self.nextRoll)
            self.addButton(text = "New game", row = 2,column = 1,command = self.newGame)
            self.refreshImages()
        def nextRoll(self):
            self.die1.roll()
            self.die2.roll()
            total = self.die1.getValue() + self.die2.getValue()
            self.stateLabel["text"] = "Total = " + str(total)
            self.refreshImages()

        def newGame(self):
            self.die1 = Die()
            self.die2 = Die()
            self.stateLabel["text"] = ""
            self.refreshImages()

        def refreshImages(self):
            fileName1 = "DICE/" + str(self.die1) + "-1.gif"
            fileName2 = "DICE/" + str(self.die2) + "-1.gif"
            self.image1 = PhotoImage(file=fileName1)
            self.dieImageLabel1["image"] = self.image1
            self.image2 = PhotoImage(file=fileName2)
            self.dieImageLabel2["image"] = self.image2

def main():
    DiceDemo().mainloop()
if __name__ == "__main__":
    main()