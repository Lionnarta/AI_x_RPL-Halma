import Board
import Player


class GameState:
    def __init__(self, Board, Player1, Player2):
        self.board = Board
        self.currentPlayer = Player1
        self.oppositePlayer = Player2
