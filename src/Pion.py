from Cell import Cell


class Pion:
    """
    Class untuk tiap pion yang ada
    - pionId = identifikasi untuk memudahkan nanti dalam menggerakkan pion
    - currentPosition = posisi pion saat ini
    """
    def __init__(self, pionOwner, currentPosition):
        """ Pion Constructor """
        self.pionOwner = pionOwner
        self.currentPosition = currentPosition

    def move(self, posisi, board):
        """ Melakukan perpindahan posisi dari currentPosition ke posisi baru pada board """
        if self.isValidMove(posisi, board):
            # Set cell menjadi kosong, yaitu tidak ada pion yang menempati (0)
            board.cell[self.currentPosition.x][
                self.currentPosition.y].setOwner(0)

            # Assign dengan posisi baru
            self.currentPosition = posisi
            board.cell[posisi.x][posisi.y].setOwner(self.pionOwner)

    def isValidMove(self, posisi, board):
        """ Cell constructor """
        # Posisi out of range
        if self.isOutRange(posisi, board):
            return False

        # Posisi diisi pion lain
        if self.isThisHaveOwner(posisi, board):
            return False

        # Memastikan kalau sudah masuk tidak boleh keluar dan sebaliknya
        if self.isFalseRegion(posisi, board):
            return False
        return True

    def isOutRange(self, posisi, board):
        """ Mengembalikan True apabila posisi baru ada di luar rentang board """
        if posisi.x < 0 or posisi.x >= board.size or posisi.y < 0 or posisi.y >= board.size:
            return True
        else:
            return False

    def isThisHaveOwner(self, posisi, board):
        """ Mengembalikan True apabila posisi pada board sudah diisi oleh pion lain """
        if board.cell[posisi.x][posisi.y].owner != 0:
            return True
        else:
            return False

    def isFalseRegion(self, posisi, board):
        """ 
        Mengembalikan True apabila ketika sudah keluar markas sendiri ingin masuk kembali
        Mengembalikan True apabila ketika sudah masuk markas lawan ingin keluar kembali
        """
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

        # Sudah masuk markas lawan, tidak boleh keluar lagi
        if (board.cell[posisi.x][posisi.y].region == 0
                or board.cell[posisi.x][posisi.y].region
                == self.pionOwner) and board.cell[self.currentPosition.x][
                    self.currentPosition.y].region == pionLawan:
            return True
        return False

    def printPion(self):
        """ Menuliskan informasi Pion ke layar terminal """
        print("Pion Owner:", self.pionOwner, end=" --> ")
        self.currentPosition.printPosisi()
