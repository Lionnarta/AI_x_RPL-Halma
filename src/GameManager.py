import Player
import Pion
import Posisi
import Board
import Cell
import Minimax

boardSize = 10


class GameManager:
    def __init__(self, boardSize):
        self.currentPlayer = Player.Player(1, boardSize)
        self.oppositePlayer = Player.Player(2, boardSize)
        self.board = Board.Board(boardSize)

    def printInfo(self):
        self.board.printBoard()

    def nextTurn(self):
        temp = self.currentPlayer
        self.currentPlayer = self.oppositePlayer
        self.oppositePlayer = temp


if __name__ == "__main__":
    boardSize = 8
    GM = GameManager(boardSize)
    GM.board.setAllPionPosition(GM.currentPlayer, GM.oppositePlayer)
    GM.printInfo()
    print("=====================================================")
    GM.currentPlayer.movePion(9, Posisi.Posisi(3, 1), GM.board)
    GM.printInfo()
    print("=====================================================")
    GM.currentPlayer.movePion(9, Posisi.Posisi(3, 2), GM.board)
    GM.printInfo()
    print("=====================================================")
    print(Minimax.Z_Function(GM.currentPlayer, boardSize))
    print(Minimax.Z_Function(GM.oppositePlayer, boardSize))