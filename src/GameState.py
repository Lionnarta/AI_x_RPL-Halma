import Board
import Player
import copy


class GameState:
    """
    Class untuk merepresentasikan state dari permainan.
    - board = menyimpan informasi board pada state tertentu
    - currentPlayer = menyimpan informasi currentPlayer pada state tertentu
    - oppositePlayer = menyimpan informasi oppositePlayer pada state tertentu
    Menggunakan teknik deep copy karena mengcopy state dari state sekarang kedalam class GameState
    Menghindari terjadinya copy by reference
    GameState digunakan dalam operasi Minimax dan Minimax with Local Search
    """
    def __init__(self, Board, Player1, Player2):
        """ GameState constructor """
        self.board = copy.deepcopy(Board)
        self.currentPlayer = copy.deepcopy(Player1)
        self.oppositePlayer = copy.deepcopy(Player2)

    def save(self, textFile):
        """ Menyimpan state ke dalam textFile agar bisa diload di lain waktu """
        # Save board to text file
        f = open("../save/" + textFile, "w")
        f.write(str(self.board.size) + "\n")

        # Save player1 to text file
        f.write(str(self.currentPlayer.noPlayer) + "\n")
        for pion in self.currentPlayer.arrayPion:
            f.write(
                str(pion.currentPosition.x) + "," +
                str(pion.currentPosition.y) + "\n")

        # Save player2 to text file
        f.write(str(self.oppositePlayer.noPlayer) + "\n")
        for pion in self.oppositePlayer.arrayPion:
            f.write(
                str(pion.currentPosition.x) + "," +
                str(pion.currentPosition.y) + "\n")

        f.close()