import numpy as np
import Pion
import Posisi


class Player:
    """
    class untuk agen
    Terdiri dari pion-pion dalam board
    """
    def __init__(self, noPlayer, boardSize):
        self.noPlayer = noPlayer
        self.arrayPion = []
        if (noPlayer == 1):
            self.setPlayerOne(boardSize)
        else:
            self.setPlayerTwo(boardSize)

    def addPion(self, Pion):
        # masukan harus tipe bentukan Pion
        self.arrayPion.append(Pion)

    def printAllPion(self):
        for pion in self.arrayPion:
            pion.printPion()

    def movePion(self, pionId, posisi, board):
        self.arrayPion[pionId].move(posisi, board)

    def getPionID(self, posisi):
        for idx in range(len(self.arrayPion)):
            if (self.arrayPion[idx].currentPosition == posisi):
                return idx
        return -1

    def setPlayerOne(self, boardSize):
        mid = int(boardSize / 2)
        pionOwner = 1
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.addPion(Pion.Pion(pionOwner, Posisi.Posisi(i, j)))

    def setPlayerTwo(self, boardSize):
        mid = int(boardSize / 2)
        pionOwner = 2
        for i in range(mid, boardSize):
            for j in range(mid, i + 1):
                temp = i - j
                x = i
                y = boardSize - 1 - temp
                self.addPion(Pion.Pion(pionOwner, Posisi.Posisi(x, y)))
