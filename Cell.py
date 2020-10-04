class Cell:
    """
    class untuk merepresentasikan cell dalam Board
    """
    def __init__(self, filled, region):
        self.filled = filled
        self.region = region

    def setFilled(self, filled):
        self.filled = filled

    def setRegion(self, region):
        self.region = region

    def printInfo(self):
        if self.filled:
            character = 'T'
        else:
            character = 'F'
        print(f'({character}, {self.region})', end="")