class Posisi:
    """
    class untuk tiap posisi
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPosisi(self):
        print(f"({self.x},{self.y})")

    def euclidean(self, M):
        return ((self.x - M.x)**2 + (self.y - M.y)**2)**0.5
    
    def __eq__(self, P):
        return (self.x == P.x) and (self.y == P.y)

    def __eq__(self, P):
        return ((self.x == P.x) and (self.y == P.y))


if __name__ == "__main__":
    P1 = Posisi(0, 3)
    P2 = Posisi(4, 0)
    print(P1.Euclidean(P2))