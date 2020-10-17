import numpy as np
import Pion
import Posisi
import time


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
        idx = 0
        for pion in self.arrayPion:
            print("ID = ", idx, end=" --> ")
            pion.printPion()
            idx += 1

    def movePion(self, pionId, posisi, board):
        self.arrayPion[pionId].move(posisi, board)

    def getPionID(self, posisi):
        for idx in range(len(self.arrayPion)):
            if (self.arrayPion[idx].currentPosition == posisi):
                return idx
        return -1

    def listAllPossibleMove(self, pionId, board):
        # return berupa list dari posisi
        queuePossibleMove = []
        queueSimpul = []
        pion = self.arrayPion[pionId]
        curX = pion.currentPosition.x
        curY = pion.currentPosition.y

        # move ONE STEP for up down left right and diagonal
        for x in range(-1, 2):
            for y in range(-1, 2):
                if pion.isValidMove(Posisi.Posisi(curX + x, curY + y), board):
                    queuePossibleMove.append(Posisi.Posisi(curX + x, curY + y))

        # move JUMP for up down left right
        queueSimpul.append(pion.currentPosition)
        currentPosition = pion.currentPosition
        while queueSimpul:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if not (pion.isOutRange(
                            Posisi.Posisi(currentPosition.x + x,
                                          currentPosition.y + y), board)):
                        if pion.isThisHaveOwner(
                                Posisi.Posisi(currentPosition.x + x,
                                              currentPosition.y + y), board):
                            tempPosition = Posisi.Posisi(
                                currentPosition.x + 2 * x,
                                currentPosition.y + 2 * y)
                            if (pion.isValidMove(tempPosition, board) and
                                    (tempPosition not in queuePossibleMove)):
                                queueSimpul.append(tempPosition)
                                queuePossibleMove.append(tempPosition)
                                # Heuristics possible move
            if queueSimpul:
                newPosition = queueSimpul.pop()
                currentPosition = newPosition
        return queuePossibleMove

    def setPlayerOne(self, boardSize):
        mid = int(boardSize / 2)
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.addPion(Pion.Pion(self.noPlayer, Posisi.Posisi(i, j)))

    def setPlayerTwo(self, boardSize):
        mid = int(boardSize / 2)
        for i in range(mid, boardSize):
            for j in range(mid, i + 1):
                temp = i - j
                x = i
                y = boardSize - 1 - temp
                self.addPion(Pion.Pion(self.noPlayer, Posisi.Posisi(x, y)))

    def loadData(self, arrPosition):
        idx = 0
        for pion in self.arrayPion:
            pion.currentPosition = arrPosition[idx]
            idx += 1
