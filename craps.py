"""
    Name: Võ Viết Thanh
    Date:30/10/2021
    File: craps.py
    This module studies and plays the game of craps.
"""
from die import Die
class Player(object):
    def __init__(self):
        self.diel = Die()
        self.die2 = Die()
        self.rolls = []
    def __str__(self):
        result = ""
        for (vl, v2) in self.rolls:
            result = result + str((vl, v2)) + " " + \
            str(vl + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        return len(self.rolls)

    def play(self):
        self.rolls = []
        self.diel.roll()
        self.die2.roll()
        (vl, v2) = (self.diel.getvalue(),
        self.die2.getvalue())
        self.rolls.append((vl, v2) )
        initialSum = vl + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while True:
            self.diel.roll()
            self.die2.roll()
            (vl, v2) = (self.diel.getvalue(),
            self.die2.getvalue())
            self.rolls.append((vl, v2))
            laterSum = vl + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

def playOneGame():
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")
def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
    if hasWon:
        wins += 1
        winRolls += rolls
    else:
        losses += 1
        lossRolls += rolls
        print("The total number of wins is", wins)
        print("The total number of losses is", losses)
        print("The average number of rolls per win is %0.2f" % \
                (winRolls / wins))
        print("The average number of rolls per loss is %0.2f" % \
                (lossRolls / losses))
        print("The winning percentage is %0.3f" % \
                (wins / number))

def main():
        number = int(input("Enter the number of games: "))
        playManyGames(number)
        if __name__ == "__main__":
            main()