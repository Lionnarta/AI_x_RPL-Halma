import sys
import os
import pygame
import math
import time
from pygame.locals import *
from base_setup import *
sys.path.append('../src')
import GameManager


def coordinate_to_point(x, y, setup):
    x1 = (y + setup.get_y()) / setup.get_scale()
    y1 = (x - setup.get_x()) / setup.get_scale()
    return math.floor(x1), math.floor(y1)


def point_to_coordinate(x, y, baseSetup):
    coor_x = y * baseSetup.get_scale() + baseSetup.get_x()
    coor_y = x * baseSetup.get_scale() - baseSetup.get_y()
    return coor_x, coor_y


def matriks_to_list(matrik, setup):
    list_pion = []
    for i in range(matrik.size):
        for j in range(matrik.size):
            if matrik.cell[i][j].owner == 1:
                list_pion.append(((i + 1, j + 1), 1))
            elif matrik.cell[i][j].owner == 2:
                list_pion.append(((i + 1, j + 1), 2))
    return list_pion


def active_block_move(screen, listPossibleMove, baseSetup):
    for new_position in listPossibleMove:
        board_active = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "active_block.png"))
        board_active = pygame.transform.scale(
            board_active, (baseSetup.get_scale(), baseSetup.get_scale()))
        coor = point_to_coordinate(new_position.x + 1, new_position.y + 1,
                                   baseSetup)
        screen.blit(board_active, (coor[0], coor[1]))


def update_board(screen, setup, GM):
    list_pion = matriks_to_list(GM.board, setup)
    for item in list_pion:
        if item[1] == 1:
            image = pygame.image.load(
                os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                             "green_pawn.png"))
        elif item[1] == 2:
            image = pygame.image.load(
                os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                             "red_pawn.png"))
        image = pygame.transform.scale(image, (setup.get_scale(), setup.get_scale()))
        rect = image.get_rect()
        screen.blit(image, (setup.get_scale() * item[0][1] + setup.get_x(), setup.get_scale() * item[0][0] - setup.get_y()))

def winMessage(screen, curPlayer):
    win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
    if curPlayer == 1:
        win_img = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "win_message_1.png"))
        screen.blit(win_img, win_pos)
        pygame.display.update()
        time.sleep(3)
    else:
        win_img = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "win_message_2.png"))
        screen.blit(win_img, win_pos)
        pygame.display.update()
        time.sleep(3)


# Main game screen
def main(screen, active, boardSize, player_default, txt):
    # Setup board scaling and shifting
    setup = base_setup(0, 0, 0, 0)
    if (boardSize == 8):
        setup.set_scale(85)
        setup.set_x(86)
        setup.set_y(44)
        setup.set_status(343)
    if (boardSize == 10):
        setup.set_scale(70)
        setup.set_x(81)
        setup.set_y(34)
        setup.set_status(350)
    if (boardSize == 16):
        setup.set_scale(45)
        setup.set_x(95)
        setup.set_y(24)
        setup.set_status(363)

    GM = GameManager.GameManager(boardSize, active, int(txt), player_default)
    FONT = pygame.font.Font(None, 32)

    # Variable
    running = True
    active_click_box = False
    terminalState = False
    possible_moves = []
    time_start = time.time()
    turn = 1
    # Game loop
    while running:
        screen.fill((53, 50, 50))
        evenodd = 0

        # Setup status board
        game_status = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "game_status.png"))
        game_status_pos = Rect(screen.get_width()/2+350, screen.get_height()/2-setup.get_status(), 150, 140)
        screen.blit(game_status, game_status_pos)

        # player turn
        green_turn = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "green_pawn.png"))
        green_turn = pygame.transform.scale(green_turn, (30, 30))
        red_turn = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "red_pawn.png"))
        red_turn = pygame.transform.scale(red_turn, (30, 30))
        turn_pos = Rect(screen.get_width()/2+400, screen.get_height()/2-setup.get_status()+40, 30, 30)
        if GM.currentPlayer.noPlayer == 1:
            screen.blit(green_turn, turn_pos)
        else:
            screen.blit(red_turn, turn_pos)

        # Draw board to screen
        for i in range(1, boardSize + 1):
            for j in range(1, boardSize + 1):
                if evenodd % 2 == 0:
                    if (GM.board.cell[i - 1][j - 1].region == 0):
                        pygame.draw.rect(screen, (255, 248, 220), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                    elif (GM.board.cell[i - 1][j - 1].region == 1):
                        pygame.draw.rect(screen, (152, 251, 152), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                    elif (GM.board.cell[i - 1][j - 1].region == 2):
                        pygame.draw.rect(screen, (240, 128, 128), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                else:
                    if (GM.board.cell[i - 1][j - 1].region == 0):
                        pygame.draw.rect(screen, (222, 184, 135), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                    elif (GM.board.cell[i - 1][j - 1].region == 1):
                        pygame.draw.rect(screen, (60, 179, 113), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                    elif (GM.board.cell[i - 1][j - 1].region == 2):
                        pygame.draw.rect(screen, (220, 20, 60), [
                            setup.get_scale() * j + setup.get_x(),
                            setup.get_scale() * i - setup.get_y(),
                            setup.get_scale(),
                            setup.get_scale()
                        ])
                evenodd += 1
            evenodd -= 1

        # Getter mouse coordinates -> Tuple X, Y
        mouse = pygame.mouse.get_pos()
        update_board(screen, setup, GM)

        if active_click_box:
            active_block_move(screen, possible_moves, setup)

        # Ketika currentPlayer adalah bukan giliran manusia, melainkan giliran BOT
        if (GM.currentPlayer.noPlayer != player_default):
            # Mode permainan adalah Player vs BOT Minimax
            if (active == 1):
                update_board(screen, setup, GM)
                pygame.display.update()
                terminalState = GM.minimaxMove()
                update_board(screen, setup, GM)
                pygame.display.update()
                if terminalState == True:
                    print("Player " + str(GM.currentPlayer.noPlayer) + " Minimax win the game!")
                    win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
                    winMessage(screen, GM.currentPlayer.noPlayer)
                    running = False
                else:
                    GM.nextTurn()
                    turn += 1
            # Mode permainan adalah Player vs BOT Minimax Local Search
            elif (active == 2):
                update_board(screen, setup, GM)
                pygame.display.update()
                terminalState = GM.minimaxLocalSearchMove()
                update_board(screen, setup, GM)
                pygame.display.update()
                if terminalState == True:
                    print("Player " + str(GM.currentPlayer.noPlayer) + " Minimax Local Search win the game!")
                    win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
                    winMessage(screen, GM.currentPlayer.noPlayer)
                    running = False
                else:
                    GM.nextTurn()
                    turn += 1
        
        # Ketika mode permainan adalah BOT Minimax vs BOT Minimax Local Search
        if (active == 3):
            if (GM.currentPlayer.noPlayer == 1):
                update_board(screen, setup, GM)
                pygame.display.update()
                terminalState = GM.minimaxMove()
                update_board(screen, setup, GM)
                pygame.display.update()
                if terminalState == True:
                    print("Player " + str(GM.currentPlayer.noPlayer) + " Minimax win the game!")
                    win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
                    winMessage(screen, GM.currentPlayer.noPlayer)
                    running = False
                else:
                    GM.nextTurn()
                    turn += 1
            else:
                update_board(screen, setup, GM)
                pygame.display.update()
                terminalState = GM.minimaxLocalSearchMove()
                update_board(screen, setup, GM)
                pygame.display.update()
                if terminalState == True:
                    print("Player " + str(GM.currentPlayer.noPlayer) + " Minimax Local Search win the game!")
                    win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
                    winMessage(screen, GM.currentPlayer.noPlayer)
                    running = False
                else:
                    GM.nextTurn()
                    turn += 1

        # Time
        time_run = math.floor(time.time() - time_start)
        time_def = str(int(txt) - time_run)
        time_to_gui = FONT.render(time_def, True, Color(0,0,0))
        time_pos = Rect(screen.get_width()/2+400, screen.get_height()/2-setup.get_status()+80, 30, 30)
        screen.blit(time_to_gui, time_pos)

        # Counting turn
        c_turn = FONT.render(str(turn), True, Color(0,0,0))
        c_turn_pos = Rect(screen.get_width()/2+400, screen.get_height()/2-setup.get_status()+115, 30, 30)
        screen.blit(c_turn, c_turn_pos)

        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if (setup.get_scale() + setup.get_x() <= mouse[0] <=
                        setup.get_scale() * (boardSize + 1) + setup.get_x()
                        and setup.get_scale() - setup.get_y() <= mouse[1] <=
                        setup.get_scale() * (boardSize + 1) - setup.get_y()):
                    # if(coordinate_to_point(mouse[0], mouse[1], setup)):

                    print(coordinate_to_point(mouse[0], mouse[1], setup))

                    # Pass ID ke BackEnd
                    x, y = coordinate_to_point(mouse[0], mouse[1], setup)
                    clickedPosition = GameManager.Posisi.Posisi(x - 1, y - 1)
                    if (GM.isValidClick(clickedPosition)):
                        if possible_moves:
                            possible_moves = []
                        possible_moves, clickedID = GM.clickedPositionToMoves(
                            clickedPosition)
                        active_click_box = True
                    if active_click_box and clickedPosition in possible_moves:
                        active_click_box = False
                        terminalState = GM.executeTheClickedMove(
                            clickedID, clickedPosition)
                        update_board(screen, setup, GM)
                        pygame.display.update()
                        if terminalState == True:
                            print("Player " + str(GM.currentPlayer.noPlayer) + " win the game!")
                            win_pos = Rect(screen.get_width()/2-150, screen.get_height()/2-90, 300, 180)
                            winMessage(screen, GM.currentPlayer.noPlayer)
                            running = False
                        time_start = time.time()
                        GM.nextTurn()

        # Update
        pygame.display.update()