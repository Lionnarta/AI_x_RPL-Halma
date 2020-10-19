from Cell import Cell


class Board:
    """
    Class untuk merepresentasikan Board dari Halma
    - size = ukuran dari board permainan halma
    - cell = kumpulan sel-sel dalam matriks berukuran size x size
    """
    def __init__(self, N):
        """ Constructor untuk class Board """
        self.size = N
        self.cell = [[Cell(0, 0) for j in range(N)] for i in range(N)]
        self.startState()

    def printBoard(self):
        """ Menuliskan board ke layar terminal """
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                self.cell[i][j].printInfo()
                print("\t", end="|")
            print()

    def startState(self):
        """ Inisialisasi Board pada awal permainan """
        self.setRegionOne()
        self.setRegionTwo()

    def setRegionOne(self):
        """ Menginisialisasi daerah dan cell-cell player One """
        mid = int(self.size / 2)
        for i in range(mid):
            for j in range(mid):
                if (i + j < mid):
                    self.cell[i][j].setRegion(1)

    def setRegionTwo(self):
        """ Menginisialisasi daerah dan cell-cell player Twos """
        mid = int(self.size / 2)
        for i in range(mid, self.size):
            for j in range(mid, i + 1):
                temp = i - j
                self.cell[i][self.size - 1 - temp].setRegion(2)

    def setAllPionPosition(self, Player1, Player2):
        """ Assign setiap posisi dari Pion Player1 dan Player2 pada cell-cell board """
        for pion in Player1.arrayPion:
            self.cell[pion.currentPosition.x][pion.currentPosition.y].setOwner(
                Player1.noPlayer)
        for pion in Player2.arrayPion:
            self.cell[pion.currentPosition.x][pion.currentPosition.y].setOwner(
                Player2.noPlayer)

    def checkTerminalState(self, noPlayer):
        """ Mengecek apakah kondisi board sudah pada terminal state """
        if (noPlayer == 1):
            mid = int(self.size / 2)
            for i in range(mid, self.size):
                for j in range(mid, i + 1):
                    temp = i - j
                    if (self.cell[i][self.size - 1 - temp].owner
                            == 2) or (self.cell[i][self.size - 1 - temp].owner
                                      == 0):
                        return False
            return True

        elif (noPlayer == 2):
            mid = int(self.size / 2)
            for i in range(mid):
                for j in range(mid):
                    if (i + j < mid):
                        if (self.cell[i][j].owner
                                == 1) or (self.cell[i][j].owner == 0):
                            return False
            return True


# Board Code Testing
if __name__ == "__main__":
    A = Board(10)
    A.printBoard()
