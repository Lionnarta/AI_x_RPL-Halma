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

    def movePion(self, pionId, posisi):
        # masukkan harus berupa tipe bentukkan posisi
        # for pion in self.arrayPion:
        #     if pion.pionId == pionId:
        #         pion.currentPosition = posisi
        #         break
        self.arrayPion[pionId].move(posisi)

    def setPlayerOne(self, boardSize):
        mid = int(boardSize / 2)
        pionID = 0
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.addPion(
                        Pion.Pion(pionID, Posisi.Posisi(i, j),
                                  Posisi.Posisi(i, j)))
                    pionID += 1

    def setPlayerTwo(self, boardSize):
        mid = int(boardSize / 2)
        pionID = 0
        for i in range(mid, boardSize):
            for j in range(mid, i + 1):
                temp = i - j
                x = i
                y = boardSize - 1 - temp
                self.addPion(
                    Pion.Pion(pionID, Posisi.Posisi(x, y), Posisi.Posisi(x,
                                                                         y)))
