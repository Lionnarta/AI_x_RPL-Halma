class Cell:
    """
    Class untuk merepresentasikan cell dalam Board
    - owner = kepemilikan dari pion yang menempati cell tersebut (0 untuk kosong, 1 untuk player1, 2 untuk player2)
    - region = representasi daerah berdasarkan player1 (1), player2 (2), atau netral (0)
    """
    def __init__(self, owner, region):
        """ Cell constructor """
        self.owner = owner  # owner adalah ini cell  terisi pion player 1 atau milik player 2
        self.region = region  # region adalah ini daerah milik player 1 atau milik player 2

    def setOwner(self, owner):
        """ Mengganti owner dari cell """
        self.owner = owner

    def setRegion(self, region):
        """ Mengganti region dari cell """
        self.region = region

    def printInfo(self):
        """ Mencetak info dari cell ke layar """
        print(f'({self.owner}, {self.region})', end="")
