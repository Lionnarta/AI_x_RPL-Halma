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
    
    sumCurrentPlayer = 0
    sumOppositePlayer = 0

    if (currentPlayer.noPlayer == 1):
        for Pion in Player.arrayPion:
            sumCurrentPlayer += Pion.currentPosition.euclidean(EndPointPlayer1)
        for Pion in Player.arrayPion:
            sumOppositePlayer += Pion.currentPosition.euclidean(EndPointPlayer2)
    
    if (currentPlayer.noPlayer == 2):
        for Pion in Player.arrayPion:
            sumCurrentPlayer += Pion.currentPosition.euclidean(EndPointPlayer2)
        for Pion in Player.arrayPion:
            sumOppositePlayer += Pion.currentPosition.euclidean(EndPointPlayer1)

    if (maxEntity == 1):
        return -sumCurrentPlayer + sumOppositePlayer
    else:
        return -sumOppositePlayer + sumCurrentPlayer


def getBestMove(listOfPossibleMoves, gamestate):
    """
    Local Search dalam Algoritma Minimax with Local Search
    Local Search digunakan untuk menyederhanakan branching dari Minimax Tree yang dibangun menjadi lebih sederhana, dari
    kumpulan aksi valid menjadi suatu aksi tunggal terbaik yang bisa dilakukan oleh PionID pada suatu gamestate
    Heuristic function = Euclidean(possiblemove, M)
    Dimana M adalah titik acuan terujung (0,0) untuk player 2 dan (N-1, N-1) untuk player 1
    """
    queue = []
    if listOfPossibleMoves:
        maximum = -math.inf
        posisi = Posisi.Posisi(-999, -999)

        # Kalau currentPlayer adalah player 1, titik acuan adalah (boardSize-1, boardSize-1)
        if (gamestate.currentPlayer.noPlayer == 1):
            M = Posisi.Posisi(gamestate.boardSize - 1, gamestate.boardSize - 1)

        # Kalau currentPlayer adalah player 2, titik acuan adalah (0, 0)
        else:
            M = Posisi.Posisi(0, 0)

        # Mengambil aksi tunggal terbaik berdasarkan heuristic function
        for i in listOfPossibleMoves:
            value = i.euclidean(M)
            if value > maximum:
                posisi = i
                maximum = value
        return queue.append(posisi)


def minimax(gamestate, isCurr, depth, timeTotal, alpha, beta, maxEntity):
    """
    Algoritma Minimax yang akan dijalankan oleh BOT Minimax
    - Basis : return gamestate dan U_Function apabila time exceeded, depth == 0, dan terminalState
    - Rekurens : branching sebanyak N possible moves dan rekursif minmax berdasarkan giliran player
    """
    #HARAP DIPERHATIKAN UNTUK MASUKAN INISIALISASI AWAL
    #gamestate adalah gamestate SEKARANG
    #isCurr TRUE jika saat minimax dijalankan adalah currentPalyer=1
    #depth diisi DEPTH LIMIT
    #timeTotal diisi time.time() + TIME LIMIT(tLimit)
    #alpha diisi -inf beta inf

    # Basis
    # Ketika udah mencapai terminal
    if time.time(
    ) > timeTotal or depth == 0 or gamestate.board.checkTerminalState(
            gamestate.currentPlayer.noPlayer):
        return gamestate, U_Function(gamestate.currentPlayer, gamestate.oppositePlayer, 
                                     gamestate.board.size, maxEntity)

    # Rekurens
    # Ketika giliran player 1
    if isCurr:
        maxEval = -math.inf
        for i in range(len(gamestate.currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(i, gamestate.board)
            
            for moves in all_possible_moves_of_pion:
                # Execute the move and store it to the new gamestate
                # I.S = move dan initial gamestate
                # F.S = new gamestate
                # Setelah udah jalan, berubah ke gamestate berikutnya (next turn)
                # newGameState = suatu hasil proses pengolahan diatas

                newGameState = GameState.GameState(gamestate.board,
                                                   gamestate.currentPlayer,
                                                   gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(i, moves,
                                                    newGameState.board)
                print(f"=========== Depth = {depth}; PionID = {i} ===========")
                newGameState.board.printBoard()
                oldGameState, utility = minimax(newGameState, False, depth - 1,
                                                timeTotal, alpha, beta, maxEntity)
                maxEval = max(maxEval, utility)

                # Alpha Beta Pruning
                alpha = max(alpha, maxEval)
                if (beta <= alpha):
                    break
        print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
        newGameState.board.printBoard()
        print("======================================================================")
        return newGameState, maxEval

    # Ketika giliran player 2 (lawan)
    else:
        minEval = math.inf
        for i in range(len(gamestate.currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(
                i, gamestate.board)
            for moves in all_possible_moves_of_pion:
                # Execute the move and store it to the new gamestate
                # I.S = move dan initial gamestate
                # F.S = new gamestate
                # Setelah udah jalan, berubah ke gamestate berikutnya (next turn)
                # newGameState = suatu hasil proses pengolahan diatas
                
                newGameState = GameState.GameState(gamestate.board,
                                                   gamestate.currentPlayer,
                                                   gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(i, moves,
                                                    newGameState.board)
                print(f"=========== Depth = {depth}; PionID = {i} ===========")
                newGameState.board.printBoard()
                oldGameState, utility = minimax(newGameState, True, depth - 1,
                                                timeTotal, alpha, beta, maxEntity)

                minEval = min(minEval, utility)

                # Alpha Beta Pruning
                beta = min(beta, minEval)
                if (beta <= alpha):
                    break
    
        print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
        newGameState.board.printBoard()
        print("======================================================================")
        return newGameState, minEval


def minimaxLocalSearch(gamestate, isCurr, depth, timeTotal, alpha, beta, maxEntity):
    if time.time(
    ) > timeTotal or depth == 0 or gamestate.board.checkTerminalState(
            gamestate.currentPlayer.noPlayer):
        return gamestate, U_Function(gamestate.currentPlayer, gamestate.oppositePlayer, 
                                     gamestate.board.size, maxEntity)

    # Rekurens
    # Ketika giliran player 1
    if isCurr:
        maxEval = -math.inf
        for i in range(len(gamestate.currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(i, gamestate.board)
            moves = getBestMove(all_possible_moves_of_pion,gamestate)
            newGameState = GameState.GameState(gamestate.board,
                                                gamestate.currentPlayer,
                                                gamestate.oppositePlayer)
            newGameState.currentPlayer.movePion(i, moves,
                                                newGameState.board)
            print(f"=========== Depth = {depth}; PionID = {i} ===========")
            newGameState.board.printBoard()
            oldGameState, utility = minimax(newGameState, False, depth - 1,
                                            timeTotal, alpha, beta, maxEntity)
            maxEval = max(maxEval, utility)

            # Alpha Beta Pruning
            alpha = max(alpha, maxEval)
            if (beta <= alpha):
                break
        print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
        newGameState.board.printBoard()
        print("======================================================================")
        return newGameState, maxEval

    # Ketika giliran player 2 (lawan)
    else:
        minEval = math.inf
        for i in range(len(gamestate.currentPlayer.arrayPion)):
            # Generate all possible actions for each pion
            all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(
                i, gamestate.board)
            all_possible_moves_of_pion = gamestate.currentPlayer.listAllPossibleMove(i, gamestate.board)
            moves = getBestMove(all_possible_moves_of_pion,gamestate)
                
            newGameState = GameState.GameState(gamestate.board,
                                                gamestate.currentPlayer,
                                                gamestate.oppositePlayer)
            newGameState.currentPlayer.movePion(i, moves,
                                                newGameState.board)
            print(f"=========== Depth = {depth}; PionID = {i} ===========")
            newGameState.board.printBoard()
            oldGameState, utility = minimax(newGameState, True, depth - 1,
                                            timeTotal, alpha, beta, maxEntity)

            minEval = min(minEval, utility)

            # Alpha Beta Pruning
            beta = min(beta, minEval)
            if (beta <= alpha):
                break
    
        print(f"=========== FINAL RETURN in Depth = {depth}; PionID = {i} ===========")
        newGameState.board.printBoard()
        print("======================================================================")
        return newGameState, minEval
