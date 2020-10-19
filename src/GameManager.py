import Player
import Pion
import Posisi
import Board
import Cell
import GameState
import Minimax
import time
import math


class GameManager:
    """
    Class untuk merepresentasikan Game Manager.
    GameManager berfungsi untuk mengatur alur dari permainan dan menyimpan seluruh informasi penting suatu permainan
    - currentPlayer = informasi dari player yang sedang menjadi gilirannya untuk bermain
    - oppositePlayer = informasi dari player yang sedang tidak bermain / player lawan
    - board = informasi dari papan permainan Halma yang digunakan
    - choice = pilihan mode permainan (terdapat 4 mode permainan)
    - tlimit = informasi batasan waktu per giliran / ronde permainan
    - hplayer = pilihan player 1 (hijau) atau player 2 (merah) dari pemain manusia apabila merupakan mode manusia
    """
    def __init__(self, boardSize, choice, tlimit, hplayer):
        """ Game Manager Constructor """
        self.currentPlayer = Player.Player(1, boardSize)
        self.oppositePlayer = Player.Player(2, boardSize)
        self.board = Board.Board(boardSize)
        self.board.setAllPionPosition(self.currentPlayer, self.oppositePlayer)
        self.choice = choice
        self.tlimit = tlimit
        self.hplayer = hplayer

    def printInfo(self):
        """ Mencetak informasi board dan giliran player dari sebuah permainan """
        self.board.printBoard()

    def nextTurn(self):
        """ Switch giliran pemain setelah currentPlayer terakhir mengambil langkah """
        temp = self.currentPlayer
        self.currentPlayer = self.oppositePlayer
        self.oppositePlayer = temp

    def loadMenu(self):
        """ Pilihan untuk load sebuah permainan dari save state sebelumnya pada file save text """
        print(
            "Do you want to load the existing game? Tekan ENTER bila ingin new game!",
            end=" ")
        response = input()
        if (len(response) > 0):
            textFile = input("Masukkan nama file yang ingin diload: ")
            self.loadGame(textFile)
            print("LOAD GAME SUCCESSFULLY!", end="\n\n")

    def saveGame(self):
        """ Pilihan untuk save sebuah permainan ke dalam sebuah textFile """
        textFile = input("Masukkan nama file sebagai output save game: ")
        GS = GameState.GameState(self.board, self.currentPlayer,
                                 self.oppositePlayer)
        GS.save(textFile)
        print("SAVE GAME SUCCESSFULLY!", end="\n\n")

    def loadGame(self, textFile):
        """ Load sebuah saved state ke dalam GameManager """
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

    def startGame(self):
        """ Menampilkan menu awal permainan dan eksekusi permainan berdasarkan mode permainan """
        self.loadMenu()
        if (self.choice == 1):
            self.playerVsMinMax()
        elif (self.choice == 2):
            self.playerVsMinMaxLocalSearch()
        elif (self.choice == 3):
            self.multiBot()
        elif (self.choice == 4):
            self.multiPlayer()

    # =======================================================
    # GUI / GRAPHICAL USER INTERFACE GAME EXECUTION
    # =======================================================
    def minimaxMove(self):
        """ Menjalankan bot Minimax pada giliran bot tersebut """
        print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX TURN!")
        self.currentPlayer.printAllPion()
        # Minimax Process
        beforeProcess = time.time()
        currentState = GameState.GameState(self.board, self.currentPlayer,
                                           self.oppositePlayer)
        minimaxState, _eval = Minimax.minimax(currentState, 3,
                                              time.time() + self.tlimit, -math.inf,
                                              math.inf, self.currentPlayer.noPlayer)
        deltaTime = time.time() - beforeProcess
        print(f"Execution time = {deltaTime} seconds")
        self.assignState(minimaxState)
    
    def minimaxLocalSearchMove(self):
        """ Menjalankan bot Minimax pada giliran bot tersebut """
        print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX LOCAL SEARCH TURN!")
        self.currentPlayer.printAllPion()
        # Minimax Process
        beforeProcess = time.time()
        currentState = GameState.GameState(self.board, self.currentPlayer,
                                           self.oppositePlayer)
        minimaxState, _eval = Minimax.minimaxLocalSearch(currentState, 3,
                                              time.time() + self.tlimit, -math.inf,
                                              math.inf, self.currentPlayer.noPlayer)
        deltaTime = time.time() - beforeProcess
        print(f"Execution time = {deltaTime} seconds")
        self.assignState(minimaxState)

    def isValidClick(self, position):
        """ Mengembalikan true apabila user mengclick pion yang bukan miliknya """
        clickedCell = self.board.cell[position.x][position.y]
        if (clickedCell.owner == self.currentPlayer.noPlayer):
            return True
        else:
            return False

    def clickedPositionToMoves(self, position):
        """ Mengembalikan daftar possible move pada pion pada position yang diclick oleh user """
        print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
        chosenID = self.currentPlayer.getPionID(position)
        possible_moves = self.currentPlayer.listAllPossibleMove(
            chosenID, self.board)
        return possible_moves, chosenID

    def executeTheClickedMove(self, chosenID, position):
        """ Mengeksekusi possible move pada pion chosenID yang dipilih ke posisi baru yaitu position """
        self.currentPlayer.movePion(chosenID, position, self.board)
        terminalState = False
        if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
            terminalState = True
        return terminalState

    def assignState(self, newState):
        """ Assign State baru dari Game Manager setelah BOT mengambil langkah """
        self.currentPlayer = newState.currentPlayer
        self.oppositePlayer = newState.oppositePlayer
        self.board = newState.board

    # =======================================================
    # COMMAND PROMPT BASED / TERMINAL GAME EXECUTION
    # =======================================================
    def playerVsMinMax(self):
        """ Permainan Mode 1: Player vs BOT Minimax """
        terminalState = False
        while not (terminalState):
            self.printInfo()

            # Giliran Player BOT Minimax
            if (self.currentPlayer.noPlayer != self.hplayer):
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX TURN!")
                input("Begin minimax? ")
                self.currentPlayer.printAllPion()

                # Minimax process for the BOT
                currentState = GameState.GameState(self.board, self.currentPlayer, self.oppositePlayer)
                beforeProcess = time.time()
                minimaxState, _eval = Minimax.minimax(currentState, 2, time.time() + self.tlimit, -math.inf, math.inf, self.currentPlayer.noPlayer)
                self.assignState(minimaxState)
                deltaTime = time.time() - beforeProcess
                print(f"Execution time = {deltaTime} seconds")
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " FANO")
                print("PLAYER " + str(self.hplayer) + " Hello")
                input("Boleh next sekarang!")

            # Giliran Player Manusia
            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
                self.currentPlayer.printAllPion()
                chosenID = int(input("Pilih Pion ID mana yang ingin dimainkan :  "))
                if (chosenID == 999):
                    self.saveGame()
                possible_moves = self.currentPlayer.listAllPossibleMove(chosenID, self.board)
                for i in range(len(possible_moves)):
                    print(str(i + 1) + ". ", end="")
                    possible_moves[i].printPosisi()
                chosenMove = int(input("Pilih move yang diinginkan dengan memasukkan nomor :  "))
                self.currentPlayer.movePion(chosenID, possible_moves[chosenMove - 1], self.board)

            # Cek apakah sekarang merupakan kondisi terminal
            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()

        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def playerVsMinMaxLocalSearch(self):
        """ Permainan Mode 2: Player vs BOT Minimax Local Search """
        terminalState = False
        while not (terminalState):
            self.printInfo()

            # Giliran Player BOT Minimax Local Search
            if (self.currentPlayer.noPlayer != self.hplayer):
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX LOCAL SEARCH TURN!")
                self.currentPlayer.printAllPion()

                # Minimax Local Search process for the BOT
                currentState = GameState.GameState(self.board, self.currentPlayer, self.oppositePlayer)
                beforeProcess = time.time()
                minimaxState, _eval = Minimax.minimaxLocalSearch(currentState, 3, time.time() + self.tlimit, -math.inf, math.inf, self.currentPlayer.noPlayer)
                self.assignState(minimaxState)
                deltaTime = time.time() - beforeProcess
                print(f"Execution time = {deltaTime} seconds")

            # Giliran Player Manusia
            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " TURN!")
                self.currentPlayer.printAllPion()
                chosenID = int(input("Pilih Pion ID mana yang ingin dimainkan :  "))
                if (chosenID == 999):
                    self.saveGame()
                possible_moves = self.currentPlayer.listAllPossibleMove(chosenID, self.board)
                for i in range(len(possible_moves)):
                    print(str(i + 1) + ". ", end="")
                    possible_moves[i].printPosisi()
                chosenMove = int(input("Pilih move yang diinginkan dengan memasukkan nomor :  "))
                self.currentPlayer.movePion(chosenID, possible_moves[chosenMove - 1], self.board)

            # Cek apakah sekarang merupakan kondisi terminal
            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()

        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def multiBot(self):
        """ Permainan Mode 3: Bot Minimax vs Bot Minimax Local Search"""
        terminalState = False
        while not (terminalState):
            # Masukkan mau pion ID berapa yang mau dijalankan
            self.printInfo()
            if (self.currentPlayer.noPlayer == 1):
                print("PLAYER " + str(self.currentPlayer.noPlayer) +
                      " MINIMAX TURN!")
                self.currentPlayer.printAllPion()
                # Minimax Process
                currentState = GameState.GameState(self.board, self.currentPlayer, self.oppositePlayer)
                beforeProcess = time.time()
                minimaxState, _eval = Minimax.minimax(currentState, 3, time.time() + self.tlimit, -math.inf, math.inf, self.currentPlayer.noPlayer)
                self.assignState(minimaxState)
                deltaTime = time.time() - beforeProcess
                print(f"Execution time = {deltaTime} seconds")

            else:
                print("PLAYER " + str(self.currentPlayer.noPlayer) + " MINIMAX LOCAL SEARCH TURN!")
                self.currentPlayer.printAllPion()
                # Minimax with Local Search
                currentState = GameState.GameState(self.board, self.currentPlayer, self.oppositePlayer)
                beforeProcess = time.time()
                minimaxState, _eval = Minimax.minimaxLocalSearch(currentState, 3, time.time() + self.tlimit, -math.inf, math.inf, self.currentPlayer.noPlayer)
                self.assignState(minimaxState)
                deltaTime = time.time() - beforeProcess
                print(f"Execution time = {deltaTime} seconds")

            if (self.board.checkTerminalState(self.currentPlayer.noPlayer)):
                terminalState = True
            else:
                self.nextTurn()
        self.printInfo()
        print("Player " + str(self.currentPlayer.noPlayer) + " win the game!")

    def multiPlayer(self):
        """ Permainan Mode 4: Player vs Player"""
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
    # print("Welcome to the Halma Game!")
    # print("1. Multiplayer")
    # print("2. Player vs CPU Minimax")
    # print("3. Player vs CPU Minimax Local Search")
    # print("4. CPU Minimax vs CPU Minimax Local Search")
    # choice = int(input("Masukkan pilihan mode permainan yang diinginkan: "))
    # boardSize = int(input("Pilih ukuran papan N x N dalam input bilangan N: "))
    # tlimit = int(input("Tentukan time limit untuk setiap permainan! "))
    # hplayer = 0
    # if (choice != 1) or (choice != 4):
    #     hplayer = int(
    #         input("Tentukan mau pilih Merah (1) atau Hijau (2): "))

    boardSize = 4
    choice = 1
    tlimit = 5
    hplayer = 1
    GM = GameManager(boardSize, choice, tlimit, hplayer)
    GM.startGame()