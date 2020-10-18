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


def getBestMove(listOfPossibleMoves, gamestate):
    if listOfPossibleMoves:
        maximum = -math.inf
        posisi = Posisi.Posisi(-999, -999)
        if (gamestate.currentPlayer.noPlayer == 1):
            M = Posisi.Posisi(gamestate.boardSize - 1, gamestate.boardSize - 1)
        else:
            M = Posisi.Posisi(0, 0)
        for i in listOfPossibleMoves:
            value = i.euclidean(M)
            if value > maximum:
                posisi = i
                maximum = value
        return posisi


def minimax(gamestate, isCurr, depth, timeTotal, alpha, beta):
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
        return gamestate, Z_Function(gamestate.currentPlayer,
                                     gamestate.board.size)

    # Rekurens
    # Ketika giliran player 1
    if isCurr:
        maxEval = -math.inf
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
                # print("======================" + str(depth) + "fano" + str(i) +
                #       "=======================")
                # gamestate.board.printBoard()
                newGameState.currentPlayer.movePion(i, moves,
                                                    newGameState.board)
                # print("======================" + str(depth) + "filbert" +
                #       str(i) + "=======================")
                # gamestate.board.printBoard()
                print("======================" + str(depth) + "Didalem cuy" +
                      str(i) + "=======================")
                newGameState.board.printBoard()
                oldGameState, utility = minimax(newGameState, False, depth - 1,
                                                timeTotal, alpha, beta)
                maxEval = max(maxEval, utility)
                alpha = max(alpha, maxEval)
                if (beta <= alpha):
                    break
        print("======================" + str(depth) +
              "=======================")
        newGameState.board.printBoard()
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
                # Pruningnya belum dimasukin
                # newGameState = suatu hasil proses pengolahan diatas
                newGameState = GameState.GameState(gamestate.board,
                                                   gamestate.currentPlayer,
                                                   gamestate.oppositePlayer)
                newGameState.currentPlayer.movePion(i, moves,
                                                    newGameState.board)
                print("======================" + str(depth) + "Didalem cuy" +
                      str(i) + "=======================")
                newGameState.board.printBoard()
                oldGameState, utility = minimax(newGameState, True, depth - 1,
                                                timeTotal, alpha, beta)

                minEval = min(minEval, utility)
                beta = min(beta, minEval)
                if (beta <= alpha):
                    break
        print("======================" + str(depth) +
              "=======================")
        newGameState.board.printBoard()
        return newGameState, minEval
