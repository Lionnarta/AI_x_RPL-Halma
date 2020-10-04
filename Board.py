from Cell import Cell


class Board:
    """
    class untuk merepresentasikan Board dari Halma
    """
    def __init__(self, N):
        self.size = N
        self.cell = [[Cell(False, 0) for j in range(N)] for i in range(N)]
        self.startState()

    def printBoard(self):
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                self.cell[i][j].printInfo()
                print("\t", end="|")
            print()

    def startState(self):
        self.setPlayerOne()
        self.setPlayerTwo()

    def setPlayerOne(self):
        mid = int(self.size / 2)
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.cell[i][j].setFilled(True)
                    self.cell[i][j].setRegion(1)

    def setPlayerTwo(self):
        mid = int(self.size / 2)
        for i in range(mid, self.size):
            for j in range(mid, i + 1):
                temp = i - j
                self.cell[i][self.size - 1 - temp].setFilled(True)
                self.cell[i][self.size - 1 - temp].setRegion(2)


if __name__ == "__main__":
    A = Board(4)
    A.printBoard()
