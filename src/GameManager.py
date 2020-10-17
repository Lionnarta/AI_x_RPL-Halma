import Player
import Pion
import Posisi
import Board
import Cell
import GameState
# import Minimax

boardSize = 4


class GameManager:
    def __init__(self, boardSize):
        self.currentPlayer = Player.Player(1, boardSize)
        self.oppositePlayer = Player.Player(2, boardSize)
        self.board = Board.Board(boardSize)
        self.board.setAllPionPosition(self.currentPlayer, self.oppositePlayer)

    def printInfo(self):
        self.board.printBoard()

    def nextTurn(self):
        temp = self.currentPlayer
        self.currentPlayer = self.oppositePlayer
        self.oppositePlayer = temp

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

    def playing(self):
        print(
            "Do you want to load the existing game? Tekan ENTER bila ingin new game!",
            end=" ")
        response = input()
        if (len(response) > 0):
            textFile = input("Masukkan nama file yang ingin diload: ")
            self.loadGame(textFile)
            print("LOAD GAME SUCCESSFULLY!", end="\n\n")

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


if __name__ == "__main__":
    GM = GameManager(boardSize)
    GM.playing()