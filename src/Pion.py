from Cell import Cell


class Pion:
    """
    class untuk tiap pion yang ada
    pionId = identifikasi untuk memudahkan nanti dalam menggerakkan pion
    """
    def __init__(self, pionOwner, currentPosition, startPosition):
        self.pionOwner = pionOwner
        self.currentPosition = currentPosition
        self.startPosition = startPosition

    def move(self, posisi, board):
        # Nanti diganti dengan fungsi validasi
        validMove = True
        if validMove:
            # Current State
            board.cell[self.currentPosition.x][
                self.currentPosition.y].setOwner(0)

            # State Baru
            self.currentPosition = posisi
            board.cell[posisi.x][posisi.y].setOwner(1)

    def printPion(self):
        print("Pion ID:", self.pionOwner)
        self.currentPosition.printPosisi()
