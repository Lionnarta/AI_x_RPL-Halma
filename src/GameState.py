import Board
import Player


class GameState:
    def __init__(self, Board, Player1, Player2):
        self.board = Board
        self.currentPlayer = Player1
        self.oppositePlayer = Player2

    def save(self, textFile):
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