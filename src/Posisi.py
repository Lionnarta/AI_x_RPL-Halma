class Posisi:
    """
    class untuk tiap posisi
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPosisi(self):
        print(f"({self.x},{self.y})")
