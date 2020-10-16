import Posisi
import time
import math
import GameState
import Board
import Player


def Z_Function(Player, N):
    if (Player.noPlayer == 1):
        M = Posisi.Posisi(N - 1, N - 1)
    else:
        M = Posisi.Posisi(0, 0)
    sum = 0
    for Pion in Player.arrayPion:
        sum -= Pion.currentPosition.euclidean(M)
    return sum


def min_value():
    pass


def max_value():
    pass


def minimax(gamestate, depth, tLimit, alpha, beta):
    # I.S currentPlayer memaximizing nilai child
    max_time = time.time() + tLimit

    currentPlayer = gamestate.currentPlayer
    ...
    # Basis
    # Ketika udah mencapai terminal

    # Rekurens
    # Ketika giliran player 1 (kita)
    if (currentPlayer.noPlayer == 1):
        maxEval = -math.inf
        for i in range(len(currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = currentPlayer.listAllPossibleMove(
                i, board)
            for moves in all_possible_moves_of_pion:
                # Execute the move and store it to the new gamestate
                # I.S = move dan initial gamestate
                # F.S = new gamestate
                # Setelah udah jalan, berubah ke gamestate berikutnya (next turn)
                # Pruningnya belum dimasukin
                # newGameState = suatu hasil proses pengolahan diatas
                newCurrentPlayer = Player.Player(....)
                newGameState = GameState.GameState(board)
                utility = minimax(newGameState, depth-1, tLimit, alpha, beta)
                if (utility > maxEval):
                    maxEval = utility

    # Ketika giliran player 2 (lawan)
    else:
        minEval = math.inf
        for i in range(len(currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = currentPlayer.listAllPossibleMove(
                i, board)
            for moves in all_possible_moves_of_pion:
                # Execute the move and store it to the new gamestate
                # I.S = move dan initial gamestate
                # F.S = new gamestate
                # Setelah udah jalan, berubah ke gamestate berikutnya (next turn)
                # Pruningnya belum dimasukin
                # newGameState = suatu hasil proses pengolahan diatas
                utility = minimax(newGameState, depth-1, tLimit, alpha, beta)
                if (utility < minEval):
                    minEval = utility
        return minEval
