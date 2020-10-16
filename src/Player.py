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
                if pion.isValidMove(Posisi.Posisi(curX+x, curY+y), board):
                    queuePossibleMove.append(Posisi.Posisi(curX+x, curY+y))

        # move JUMP for up down left right
        while 1:
            expandSimpul = None
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if pion.isThisHaveOwner(Posisi.Posisi(curX+x, curY+y), board) == True:
                        if pion.isValidMove(Posisi.Posisi(curX+2*x, curY+2*y), board):
                            queueSimpul.append(
                                Posisi.Posisi(curX+2*x, curY+2*y))
            if expandSimpul:
                queuePossibleMove.append(expandSimpul)
                expandSimpul = queueSimpul.pop()
            else:
                break

        return queuePossibleMove

    def setPlayerOne(self, boardSize):
        mid = int(boardSize / 2)
        pionOwner = 1
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.addPion(
                        Pion.Pion(pionOwner, Posisi.Posisi(i, j),
                                  Posisi.Posisi(i, j)))

    def setPlayerTwo(self, boardSize):
        mid = int(boardSize / 2)
        pionOwner = 2
        for i in range(mid, boardSize):
            for j in range(mid, i + 1):
                temp = i - j
                x = i
                y = boardSize - 1 - temp
                self.addPion(
                    Pion.Pion(pionOwner, Posisi.Posisi(x, y),
                              Posisi.Posisi(x, y)))
