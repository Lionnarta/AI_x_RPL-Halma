import Posisi
import time
import math
import GameState
import Board
import Player
"""
Minimax Module
Berisi semua kumpulan fungsi dan algoritma yang dibutuhkan untuk konfigurasi modul Minimax
Terdiri atas utility function, localSearch, minimax, dan minimaxWithLocalSearch
"""


def U_Function(currentPlayer, oppositePlayer, N, maxEntity):
    """ Perhitungan utility function berdasarkan informasi pion player dan state tertentu pada permainan """
    EndPointPlayer1 = Posisi.Posisi(N - 1, N - 1)
    EndPointPlayer2 = Posisi.Posisi(0, 0)
    
    sumPionPlayer1 = 0
    sumPionPlayer2 = 0

    if (currentPlayer.noPlayer == 1):
        for Pion in currentPlayer.arrayPion:
            sumPionPlayer1 += Pion.currentPosition.euclidean(EndPointPlayer1)
        for Pion in oppositePlayer.arrayPion:
            sumPionPlayer2 += Pion.currentPosition.euclidean(EndPointPlayer2)
    
    if (currentPlayer.noPlayer == 2):
        for Pion in currentPlayer.arrayPion:
            sumPionPlayer2 += Pion.currentPosition.euclidean(EndPointPlayer2)
        for Pion in oppositePlayer.arrayPion:
            sumPionPlayer1 += Pion.currentPosition.euclidean(EndPointPlayer1)

    if (maxEntity == 1):
        return -sumPionPlayer1 + sumPionPlayer2
    else:
        return -sumPionPlayer2 + sumPionPlayer1


def getBestMove(listOfPossibleMoves, gamestate):
    """
    Local Search dalam Algoritma Minimax with Local Search
    Local Search digunakan untuk menyederhanakan branching dari Minimax Tree yang dibangun menjadi lebih sederhana, dari
    kumpulan aksi valid menjadi suatu aksi tunggal terbaik yang bisa dilakukan oleh PionID pada suatu gamestate
    Heuristic function = Euclidean(possiblemove, M)
    Dimana M adalah titik acuan terujung (0,0) untuk player 2 dan (N-1, N-1) untuk player 1
    """

    if listOfPossibleMoves:
        maximum = -math.inf
        posisi = Posisi.Posisi(-999, -999)

        # Kalau currentPlayer adalah player 1, titik acuan adalah (boardSize-1, boardSize-1)
        if (gamestate.currentPlayer.noPlayer == 1):
            M = Posisi.Posisi(gamestate.board.size - 1, gamestate.board.size - 1)

        # Kalau currentPlayer adalah player 2, titik acuan adalah (0, 0)
        else:
            M = Posisi.Posisi(0, 0)

        # Mengambil aksi tunggal terbaik berdasarkan heuristic function
        for i in listOfPossibleMoves:
            value = -i.euclidean(M)
            if value > maximum:
                posisi = i
                maximum = value
        return posisi


# def minimaxLocalSearch(gamestate, isCurr, depth, timeTotal, alpha, beta, maxEntity):
#     if time.time(
#     ) > timeTotal or depth == 0 or gamestate.board.checkTerminalState(
#             gamestate.currentPlayer.noPlayer):
#         return gamestate, U_Function(gamestate.currentPlayer, gamestate.oppositePlayer, 
#                                      gamestate.board.size, maxEntity)

#     # Rekurens
#     # Ketika giliran player 1
#     if isCurr:
#         maxEval = -math.inf
#         maxGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
#         for i in range(len(gamestate.currentPlayer.arrayPion)):
#             # Generate all possible actions for each pion
#             all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(i, gamestate.board)
#             moves = getBestMove(all_possible_moves_of_pion,gamestate)
#             newGameState = GameState.GameState(gamestate.board,
#                                                 gamestate.currentPlayer,
#                                                 gamestate.oppositePlayer)
#             newGameState.currentPlayer.movePion(i, moves,
#                                                 newGameState.board)
#             print(f"=========== Depth = {depth}; PionID = {i} ===========")
#             newGameState.board.printBoard()
#             oldGameState, utility = minimax(newGameState, depth - 1,
#                                             timeTotal, alpha, beta, maxEntity)
#             if (utility > maxEval):                                
#                 maxEval = utility
#                 maxGameState = newGameState

#             # Alpha Beta Pruning
#             alpha = max(alpha, maxEval)
#             if (beta <= alpha):
#                 break
#         print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
#         maxGameState.board.printBoard()
#         print("======================================================================")
#         return maxGameState, maxEval

#     # Ketika giliran player 2 (lawan)
#     else:
#         minEval = math.inf
#         minGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
#         for i in range(len(gamestate.currentPlayer.arrayPion)):
#             # Generate all possible actions for each pion
#             all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(
#                 i, gamestate.board)
#             all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(i, gamestate.board)
#             moves = getBestMove(all_possible_moves_of_pion,gamestate)
                
#             newGameState = GameState.GameState(gamestate.board,
#                                                 gamestate.currentPlayer,
#                                                 gamestate.oppositePlayer)
#             newGameState.currentPlayer.movePion(i, moves,
#                                                 newGameState.board)
#             print(f"=========== Depth = {depth}; PionID = {i} ===========")
#             newGameState.board.printBoard()
#             oldGameState, utility = minimax(newGameState, depth - 1,
#                                             timeTotal, alpha, beta, maxEntity)

#             if (utility < minEval):
#                 minEval = utility
#                 minGameState = newGameState
                

#             # Alpha Beta Pruning
#             beta = min(beta, minEval)
#             if (beta <= alpha):
#                 break
    
#         print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
#         minGameState.board.printBoard()
#         print("======================================================================")
#         return minGameState, minEval

def minimax(gamestate, depth, timeTotal, alpha, beta, maxEntity):
    """
    Algoritma Minimax yang akan dijalankan oleh BOT Minimax
    - Basis : return gamestate dan U_Function apabila time exceeded, depth == 0, dan terminalState
    - Rekurens : branching sebanyak N possible moves dan rekursif minmax berdasarkan giliran player
    """

    # Basis Rekursif
    if ((depth == 0) or (time.time() > timeTotal) or (gamestate.board.checkTerminalState(gamestate.currentPlayer.noPlayer))):
        return gamestate, U_Function(gamestate.currentPlayer, gamestate.oppositePlayer, gamestate.board.size, maxEntity)

    # Rekurens
    if (gamestate.currentPlayer.noPlayer == maxEntity):
        # Choose the maximum utility of the state
        # Iterate all pion and its possible moves
        maxGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
        maxValue = -math.inf
        print("fanooooo")

        # Iterate all pion index
        for idx in range(len(gamestate.currentPlayer.arrayPion)):
            all_possible_moves = gamestate.currentPlayer.listAllPossibleMove(idx, gamestate.board)

            # Iterate all possible moves of pion index
            for move in all_possible_moves:
                newGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(idx, move, newGameState.board)

                # DEBUGGING
                print(f"=========== Depth = {depth}; PionID = {idx} ===========")
                newGameState.board.printBoard()
                
                recursiveState = GameState.GameState(newGameState.board, newGameState.currentPlayer, newGameState.oppositePlayer)
                recursiveState.nextTurn()
                dummyState, utility = minimax(recursiveState, depth-1, timeTotal, alpha, beta, maxEntity)

                print(f"Utility = {utility}")

                # Compare with the old max value
                if (utility > maxValue):
                    maxValue = utility
                    maxGameState = newGameState
                
                alpha = max(alpha, maxValue)
                if (beta <= alpha):
                    return maxGameState, maxValue
        print("Giliran siapakah ini? ", maxGameState.currentPlayer.noPlayer)
        return maxGameState, maxValue

    else:
        # Choose the minimum utility of the state
        minGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
        minValue = math.inf
        print("MASUK WOI")

        # Iterate all pion index
        for idx in range(len(gamestate.currentPlayer.arrayPion)):
            all_possible_moves = gamestate.currentPlayer.listAllPossibleMove(idx, gamestate.board)

            # Iterate all possible moves of pion index
            for move in all_possible_moves:
                newGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(idx, move, newGameState.board)

                # DEBUGGING
                print(f"=========== Depth = {depth}; PionID = {idx} ===========")
                newGameState.board.printBoard()

                recursiveState = GameState.GameState(newGameState.board, newGameState.currentPlayer, newGameState.oppositePlayer)
                recursiveState.nextTurn()
                dummyState, utility = minimax(recursiveState, depth-1, timeTotal, alpha, beta, maxEntity)

                print(f"Utility = {utility}")

                # Compare with the old min value
                if (utility < minValue):
                    minValue = utility
                    minGameState = newGameState
                
                beta = min(beta, minValue)
                if (beta <= alpha):
                    return minGameState, minValue

        print("Giliran siapakah ini? ", minGameState.currentPlayer.noPlayer)        
        return minGameState, minValue

def minimaxLocalSearch(gamestate, depth, timeTotal, alpha, beta, maxEntity):
    """
    Algoritma Minimax + Local Search yang akan dijalankan oleh BOT Minimax + Local Search
    - Basis : return gamestate dan U_Function apabila time exceeded, depth == 0, dan terminalState
    - Rekurens : branching sebanyak N possible moves dan rekursif minmax berdasarkan giliran player
    """

    # Basis Rekursif
    if ((depth == 0) or (time.time() > timeTotal) or (gamestate.board.checkTerminalState(gamestate.currentPlayer.noPlayer))):
        return gamestate, U_Function(gamestate.currentPlayer, gamestate.oppositePlayer, gamestate.board.size, maxEntity)

    # Rekurens
    if (gamestate.currentPlayer.noPlayer == maxEntity):
        # Choose the maximum utility of the state
        # Iterate all pion and its possible moves
        maxGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
        maxValue = -math.inf
        print("fanoooooXXXXXXXXXXXXX")

        # Iterate all pion index
        for idx in range(len(gamestate.currentPlayer.arrayPion)):
            all_possible_moves = gamestate.currentPlayer.listAllPossibleMove(idx, gamestate.board)

            # Choose the best move from local search heuristic
            if (len(all_possible_moves) > 0):
                move = getBestMove(all_possible_moves, gamestate)
                newGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(idx, move, newGameState.board)

                # DEBUGGING
                print(f"=========== Depth = {depth}; PionID = {idx} ===========")
                newGameState.board.printBoard()
                
                recursiveState = GameState.GameState(newGameState.board, newGameState.currentPlayer, newGameState.oppositePlayer)
                recursiveState.nextTurn()
                dummyState, utility = minimaxLocalSearch(recursiveState, depth-1, timeTotal, alpha, beta, maxEntity)

                print(f"Utility = {utility}")

                # Compare with the old max value
                if (utility > maxValue):
                    maxValue = utility
                    maxGameState = newGameState
                
                alpha = max(alpha, maxValue)
                if (beta <= alpha):
                    return maxGameState, maxValue

        print("Giliran siapakah ini? ", maxGameState.currentPlayer.noPlayer)
        return maxGameState, maxValue

    else:
        # Choose the minimum utility of the state
        minGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
        minValue = math.inf
        print("MASUK WOIXXXXXXXXXXXXXXX")

        # Iterate all pion index
        for idx in range(len(gamestate.currentPlayer.arrayPion)):
            all_possible_moves = gamestate.currentPlayer.listAllPossibleMove(idx, gamestate.board)

            if (len(all_possible_moves) > 0):
                # Choose the best move from local search heuristic
                move = getBestMove(all_possible_moves, gamestate)
                newGameState = GameState.GameState(gamestate.board, gamestate.currentPlayer, gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(idx, move, newGameState.board)

                # DEBUGGING
                print(f"=========== Depth = {depth}; PionID = {idx} ===========")
                newGameState.board.printBoard()

                recursiveState = GameState.GameState(newGameState.board, newGameState.currentPlayer, newGameState.oppositePlayer)
                recursiveState.nextTurn()
                dummyState, utility = minimaxLocalSearch(recursiveState, depth-1, timeTotal, alpha, beta, maxEntity)

                print(f"Utility = {utility}")

                # Compare with the old min value
                if (utility < minValue):
                    minValue = utility
                    minGameState = newGameState
                
                beta = min(beta, minValue)
                if (beta <= alpha):
                    return minGameState, minValue

        print("Giliran siapakah ini? ", minGameState.currentPlayer.noPlayer)        
        return minGameState, minValue