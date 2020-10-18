import Player
import Pion
import Posisi
import Board
import Cell
import GameState
import Minimax
import time
import math

boardSize = 10


class GameManager:
    def __init__(self, boardSize, choice):
        self.currentPlayer = Player.Player(1, boardSize)
        self.oppositePlayer = Player.Player(2, boardSize)
        self.board = Board.Board(boardSize)
        self.board.setAllPionPosition(self.currentPlayer, self.oppositePlayer)
        self.choice = choice

    def printInfo(self):
        self.board.printBoard()

    def nextTurn(self):
        temp = self.currentPlayer
        self.currentPlayer = self.oppositePlayer
        self.oppositePlayer = temp

    def loadMenu(self):
        print(
            "Do you want to load the existing game? Tekan ENTER bila ingin new game!",
            end=" ")
        response = input()
        if (len(response) > 0):
            textFile = input("Masukkan nama file yang ingin diload: ")
            self.loadGame(textFile)
            print("LOAD GAME SUCCESSFULLY!", end="\n\n")

    def saveGame(self):
        textFile = input("Masukkan nama file sebagai output save game: ")
        GS = GameState.GameState(self.board, self.currentPlayer,
                                 self.oppositePlayer)
        GS.save(textFile)
        print("SAVE GAME SUCCESSFULLY!", end="\n\n")

    def loadGame(self, textFile):
        # Load state from text file
        f = open("../save/" + textFile, "r")
        buff = f.read()
        list_lines = buff.split("\n")
        list_lines.pop()
        boardSize = int(list_lines[0])
        self.board = Board.Board(boardSize)

        # Set the currentPlayer
        noCurPlayer = int(list_lines[1])
        self.currentPlayer = Player.Player(noCurPlayer, boardSize)
        idx = 2
        arrayPosition = []
        while ("," in list_lines[idx]):
            temp = list_lines[idx].split(",")
            arrayPosition.append(Posisi.Posisi(int(temp[0]), int(temp[1])))
            idx += 1
        self.currentPlayer.loadData(arrayPosition)

        # Set the opposite player
        noOppPlayer = int(list_lines[idx])
        idx += 1
        self.oppositePlayer = Player.Player(noOppPlayer, boardSize)
        arrayPosition = []
        n = len(list_lines)
        while (idx < n):
            temp = list_lines[idx].split(",")
            arrayPosition.append(Posisi.Posisi(int(temp[0]), int(temp[1])))
            idx += 1
        self.oppositePlayer.loadData(arrayPosition)

        # Set all pion position of currentPlayer and oppositePlayer
        self.board.setAllPionPosition(self.currentPlayer, self.oppositePlayer)
        f.close()

    def startGame(self, choice):
        self.loadMenu()
        if (choice == 1):
            self.playing()
        elif (choice == 2):
            self.playerVsMinMax()
        elif (choice == 3):
            self.playerVsMinMaxLocalSearch()
        elif (choice == 4):
            self.botVsBot()

    def minimaxMove(self):
        print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX TURN!")
        self.currentPlayer.printAllPion()
        # Minimax Process
        currentState = GameState.GameState(self.board, self.currentPlayer,
                                           self.oppositePlayer)
        minimaxState, _eval = Minimax.minimax(currentState, True, 3,
                                              time.time() + 10, -math.inf,
                                              math.inf)
        self.assignState(minimaxState)

    def isValidClick(self, position):
        clickedCell = self.board.cell[position.x][position.y]
        if (clickedCell.owner == self.currentPlayer.noPlayer):
            return True
        else:
            return False

    def clickedPositionToMoves(self, position):
        # self.printInfo()
        print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
        # self.currentPlayer.printAllPion()
        chosenID = self.currentPlayer.getPionID(position)
        # print(chosenID)
        possible_moves = self.currentPlayer.listAllPossibleMove(
            chosenID, self.board)
        # for i in range(len(possible_moves)):
        #     print(str(i + 1) + ". ", end="")
        #     possible_moves[i].printPosisi()
        return possible_moves, chosenID

    def executeTheClickedMove(self, chosenID, position):
        self.currentPlayer.movePion(chosenID, position, self.board)
        terminalState = False
        if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
            terminalState = True
        return terminalState

    def playing(self):
        terminalState = False
        while not (terminalState):
            # Masukkan mau pion ID berapa yang mau dijalankan
            self.printInfo()
            print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
            self.currentPlayer.printAllPion()
            chosenID = int(
                input("Pilih Pion ID mana yang ingin dimainkan :  "))
            if (chosenID == 999):
                self.saveGame()
            possible_moves = self.currentPlayer.listAllPossibleMove(
                chosenID, self.board)
            for i in range(len(possible_moves)):
                print(str(i + 1) + ". ", end="")
                possible_moves[i].printPosisi()
            chosenMove = int(
                input(
                    "Pilih move yang diinginkan dengan memasukkan nomor :  "))
            self.currentPlayer.movePion(chosenID,
                                        possible_moves[chosenMove - 1],
                                        self.board)
            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()
        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def botVsBot(self):
        terminalState = False
        while not (terminalState):
            # Masukkan mau pion ID berapa yang mau dijalankan
            self.printInfo()
            if (self.currentPlayer.noPlayer == 1):
                print("PLAYER " + str(self.currentPlayer.noPlayer) +
                      " MINIMAX TURN!")
                self.currentPlayer.printAllPion()
                # Minimax Process
                # minMaxID, minMaxPosition = minMaxProcess()
                # self.currentPlayer.movePion(minMaxID, minMaxPosition, self.board)
            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
                self.currentPlayer.printAllPion()
                # Minimax with Local Search
                # minMaxID, minMaxPosition = minMaxProcess()
                # self.currentPlayer.movePion(minMaxID, minMaxPosition, self.board)

            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()
        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def playerVsMinMaxLocalSearch(self):
        terminalState = False
        while not (terminalState):
            # Masukkan mau pion ID berapa yang mau dijalankan
            self.printInfo()
            if (self.currentPlayer.noPlayer == 1):
                print("PLAYER " + str(self.currentPlayer.noPlayer) +
                      " MINIMAX TURN!")
                self.currentPlayer.printAllPion()
                # Minimax Local Search
                # minMaxID, minMaxPosition = minMaxProcess()
                # self.currentPlayer.movePion(minMaxID, minMaxPosition, self.board)
            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
                self.currentPlayer.printAllPion()
                chosenID = int(
                    input("Pilih Pion ID mana yang ingin dimainkan :  "))
                if (chosenID == 999):
                    self.saveGame()
                possible_moves = self.currentPlayer.listAllPossibleMove(
                    chosenID, self.board)
                for i in range(len(possible_moves)):
                    print(str(i + 1) + ". ", end="")
                    possible_moves[i].printPosisi()
                chosenMove = int(
                    input(
                        "Pilih move yang diinginkan dengan memasukkan nomor :  "
                    ))
                self.currentPlayer.movePion(chosenID,
                                            possible_moves[chosenMove - 1],
                                            self.board)

            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()
        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def assignState(self, newState):
        self.currentPlayer = newState.currentPlayer
        self.oppositePlayer = newState.oppositePlayer
        self.board = newState.board

    def playerVsMinMax(self):
        terminalState = False
        while not (terminalState):
            # Masukkan mau pion ID berapa yang mau dijalankan
            self.printInfo()
            if (self.currentPlayer.noPlayer == 1):
                print("PLAYER " + str(self.currentPlayer.noPlayer) +
                      " MINIMAX TURN!")
                self.currentPlayer.printAllPion()
                # Minimax Process
                currentState = GameState.GameState(self.board,
                                                   self.currentPlayer,
                                                   self.oppositePlayer)
                minimaxState, _eval = Minimax.minimax(currentState, True, 3,
                                                      time.time() + 10,
                                                      -math.inf, math.inf)
                self.assignState(minimaxState)
            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
                self.currentPlayer.printAllPion()
                chosenID = int(
                    input("Pilih Pion ID mana yang ingin dimainkan :  "))
                if (chosenID == 999):
                    self.saveGame()
                possible_moves = self.currentPlayer.listAllPossibleMove(
                    chosenID, self.board)
                for i in range(len(possible_moves)):
                    print(str(i + 1) + ". ", end="")
                    possible_moves[i].printPosisi()
                chosenMove = int(
                    input(
                        "Pilih move yang diinginkan dengan memasukkan nomor :  "
                    ))
                self.currentPlayer.movePion(chosenID,
                                            possible_moves[chosenMove - 1],
                                            self.board)

            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()
        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")


if __name__ == "__main__":
    # print("Welcome to the Halma Game!")
    # print("1. Multiplayer")
    # print("2. Player vs CPU Minimax")
    # print("3. Player vs CPU Minimax Local Search")
    # print("4. CPU Minimax vs CPU Minimax Local Search")
    # choice = int(input("Masukkan pilihan mode permainan yang diinginkan: "))
    # boardSize = int(input("Pilih ukuran papan N x N dalam input bilangan N: "))
    # tlimit = int(input("Tentukan time limit untuk setiap permainan! "))
    # playerChoice = 0
    # if (choice != 1) or (choice != 4):
    #     playerchoice = int(
    #         input("Tentukan mau pilih Merah (1) atau Hijau (2): "))

    boardSize = 4
    choice = 2
    GM = GameManager(boardSize, choice)
    GM.startGame(choice)