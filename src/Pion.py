from Cell import Cell


class Pion:
    """
    class untuk tiap pion yang ada
    pionId = identifikasi untuk memudahkan nanti dalam menggerakkan pion
    """
    def __init__(self, pionOwner, currentPosition):
        self.pionOwner = pionOwner
        self.currentPosition = currentPosition

    def move(self, posisi, board):
        # Nanti diganti dengan fungsi validasi

        if self.isValidMove(posisi, board):
            # Current State
            board.cell[self.currentPosition.x][
                self.currentPosition.y].setOwner(0)

            # State Baru
            self.currentPosition = posisi
            board.cell[posisi.x][posisi.y].setOwner(self.pionOwner)

    def isValidMove(self, posisi, board):
        # Posisi out of range
        if self.isOutRange(posisi, board):
            return False
        # Posisi diisi pion lain
        if self.isThisHaveOwner(posisi, board):
            return False
        if self.isFalseRegion(posisi, board):
            return False
        return True

    def isOutRange(self, posisi, board):
        if posisi.x < 0 or posisi.x >= board.size or posisi.y < 0 or posisi.y >= board.size:
            return True
        else:
            return False

    def isThisHaveOwner(self, posisi, board):
        if board.cell[posisi.x][posisi.y].owner != 0:
            return True
        else:
            return False

    def isFalseRegion(self, posisi, board):
        # Dari luar markas mau ke markas sendiri
        if board.cell[posisi.x][
                posisi.y].region == self.pionOwner and board.cell[
                    self.currentPosition.x][
                        self.currentPosition.y].region == 0:
            return True

        # Penentuan daerah pion lawan
        pionLawan = 2
        if (self.pionOwner == 2):
            pionLawan = 1

        # Udah masuk markas lawan gak boleh keluar lagi
        if (board.cell[posisi.x][posisi.y].region == 0
                or board.cell[posisi.x][posisi.y].region
                == self.pionOwner) and board.cell[self.currentPosition.x][
                    self.currentPosition.y].region == pionLawan:
            return True
        return False

    def printPion(self):
        print("Pion Owner:", self.pionOwner, end=" --> ")
        self.currentPosition.printPosisi()
