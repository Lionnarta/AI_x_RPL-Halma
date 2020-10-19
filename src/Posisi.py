class Posisi:
    """
    Class untuk mendefinisikan posisi
    - x = vertical position (baris)
    - y = horizontal position (kolom)

    """
    def __init__(self, x, y):
        """ Constructor untuk class Posisi """
        self.x = x
        self.y = y

    def printPosisi(self):
        """ Mencetak informasi posisi ke dalam layar """
        print(f"({self.x},{self.y})")

    def euclidean(self, M):
        """ Menghitung jarak euclidean dari posisi sendiri ke posisi M """
        return ((self.x - M.x)**2 + (self.y - M.y)**2)**0.5

    def __eq__(self, P):
        """ Mendefinisikan operasi equal terhadap sesama objek Posisi """
        return ((self.x == P.x) and (self.y == P.y))


# Posisi Code Testing
if __name__ == "__main__":
    P1 = Posisi(0, 3)
    P2 = Posisi(4, 0)
    P3 = Posisi(4, 0)
    print(P1.euclidean(P2))
    print(P1 == P3)
    print(P2 == P3)