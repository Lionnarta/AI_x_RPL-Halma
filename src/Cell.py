class Cell:
    """
    class untuk merepresentasikan cell dalam Board
    """
    def __init__(self, owner, region):
        self.owner = owner
        self.region = region

    def setOwner(self, owner):
        self.owner = owner

    def setRegion(self, region):
        self.region = region

    def printInfo(self):
        print(f'({self.owner}, {self.region})', end="")