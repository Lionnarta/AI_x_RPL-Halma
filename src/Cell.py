class Cell:
    """
    class untuk merepresentasikan cell dalam Board
    """
    def __init__(self, owner, region):
        # owner adalah ini cell  player 1 atau milik player 2
        self.owner = owner
        # region adalah ini daerah milik player 1 atau milik player 2
        self.region = region

    def setOwner(self, owner):
        self.owner = owner

    def setRegion(self, region):
        self.region = region

    def printInfo(self):
        print(f'({self.owner}, {self.region})', end="")
