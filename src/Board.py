from Cell import Cell


class Board:
    """
    class untuk merepresentasikan Board dari Halma
    """

    def __init__(self, N):
        self.size = N
        self.cell = [[Cell(0, 0) for j in range(N)] for i in range(N)]
        self.startState()

    def printBoard(self):
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                self.cell[i][j].printInfo()
                print("\t", end="|")
            print()

    def startState(self):
        self.setRegionOne()
        self.setRegionTwo()

    def setRegionOne(self):
        mid = int(self.size / 2)
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.cell[i][j].setRegion(1)

    def setRegionTwo(self):
        mid = int(self.size / 2)
        for i in range(mid, self.size):
            for j in range(mid, i + 1):
                temp = i - j
                self.cell[i][self.size - 1 - temp].setRegion(2)

    def setAllPionPosition(self, Player1, Player2):
        for pion in Player1.arrayPion:
            self.cell[pion.currentPosition.x][pion.currentPosition.y].setOwner(
                Player1.noPlayer)
        for pion in Player2.arrayPion:
            self.cell[pion.currentPosition.x][pion.currentPosition.y].setOwner(
                Player2.noPlayer)


if __name__ == "__main__":
    A = Board(10)
    A.printBoard()
