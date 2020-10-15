class Pion:
    """
    class untuk tiap pion yang ada
    pionId = identifikasi untuk memudahkan nanti dalam menggerakkan pion
    """
    def __init__(self, pionId, currentPosition, startPosition):
        self.pionId = pionId
        self.currentPosition = currentPosition
        self.startPosition = startPosition

    def move(self, posisi):
        # Nanti diganti dengan fungsi validasi
        validMove = True
        if validMove:
            self.currentPosition = posisi

    def printPion(self):
        print("Pion ID:", self.pionId)
        self.currentPosition.printPosisi()
