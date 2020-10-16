import Player
import Pion
import Posisi
import Board
import Cell

boardSize = 10


class GameManager:
    def __init__(self):
        self.currentPlayer = Player.Player(1, boardSize)
        self.oppositePlayer = Player.Player(2, boardSize)
        self.board = Board.Board(boardSize)

    def printInfo(self):
        if self.currentPlayer.noPlayer == 1:
            self.board.setAllPionPosition(self.currentPlayer,
                                          self.oppositePlayer)
        else:
            self.board.setAllPionPosition(self.oppositePlayer,
                                          self.currentPlayer)
        self.board.printBoard()

    def nextTurn(self):
        temp = self.currentPlayer
        self.currentPlayer = self.oppositePlayer
        self.oppositePlayer = temp


if __name__ == "__main__":
    GM = GameManager()
    GM.printInfo()
    print("=====================================================")
    GM.currentPlayer.movePion(14, Posisi.Posisi(4, 1), GM.board)
    GM.printInfo()
    print("=====================================================")
    GM.currentPlayer.movePion(14, Posisi.Posisi(4, 2), GM.board)
    GM.printInfo()
    print("=====================================================")
