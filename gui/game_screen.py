import sys
import os
import pygame
import math
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
            image = pygame.transform.scale(
                image, (setup.get_scale(), setup.get_scale()))
            rect = image.get_rect()
            screen.blit(image,
                        (setup.get_scale() * item[0][1] + setup.get_x(),
                         setup.get_scale() * item[0][0] - setup.get_y()))
        elif item[1] == 2:
            image = pygame.image.load(
                os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                             "red_pawn.png"))
            image = pygame.transform.scale(
                image, (setup.get_scale(), setup.get_scale()))
            rect = image.get_rect()
            screen.blit(image,
                        (setup.get_scale() * item[0][1] + setup.get_x(),
                         setup.get_scale() * item[0][0] - setup.get_y()))


# Main game screen
def main(screen, active, boardSize, player_default, txt):
    # Setup board scaling and shifting
    setup = base_setup(0, 0, 0)
    if (boardSize == 8):
        setup.set_scale(85)
        setup.set_x(86)
        setup.set_y(44)
    if (boardSize == 10):
        setup.set_scale(70)
        setup.set_x(81)
        setup.set_y(34)
    if (boardSize == 16):
        setup.set_scale(45)
        setup.set_x(95)
        setup.set_y(24)

    #  Setup status board
    # game_status = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "green_pawn.png")))
    # game_status_pos = Rect(width/2+)

    GM = GameManager.GameManager(boardSize, active, int(txt), player_default)

    # Variable
    running = True
    active_click_box = False
    possible_moves = []
    terminalState = False
    # Game loop
    while running:
        screen.fill((53, 50, 50))
        evenodd = 0
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
        # List pion to gui
        # list_pion = matriks_to_list(GM.board, setup)
        # for item in list_pion:
        #     if item[1] == 1:
        #         image = pygame.image.load(
        #             os.path.join(os.path.dirname(os.getcwd()), "img",
        #                          "collection", "green_pawn.png"))
        #         image = pygame.transform.scale(
        #             image, (setup.get_scale(), setup.get_scale()))
        #         rect = image.get_rect()
        #         screen.blit(image,
        #                     (setup.get_scale() * item[0][1] + setup.get_x(),
        #                      setup.get_scale() * item[0][0] - setup.get_y()))
        #     elif item[1] == 2:
        #         image = pygame.image.load(
        #             os.path.join(os.path.dirname(os.getcwd()), "img",
        #                          "collection", "red_pawn.png"))
        #         image = pygame.transform.scale(
        #             image, (setup.get_scale(), setup.get_scale()))
        #         rect = image.get_rect()
        #         screen.blit(image,
        #                     (setup.get_scale() * item[0][1] + setup.get_x(),
        #                      setup.get_scale() * item[0][0] - setup.get_y()))

        if active_click_box:
            active_block_move(screen, possible_moves, setup)

        # Ketika currentPlayer adalah bukan giliran manusia, melainkan giliran BOT
        if (GM.currentPlayer.noPlayer != player_default):
            # Mode permainan adalah Player vs BOT Minimax
            if (active == 0):
                GM.minimaxMove()
                GM.nextTurn()
            # Mode permainan adalah Player vs BOT Minimax Local Search
            elif (active == 1):
                GM.minimaxLocalSearchMove()
                GM.nextTurn()
        
        # Ketika mode permainan adalah BOT Minimax vs BOT Minimax Local Search
        if (active == 2):
            if (GM.currentPlayer.noPlayer == 1):
                GM.minimaxMove()
                GM.nextTurn()
            else:
                GM.minimaxLocalSearchMove()
                GM.nextTurn()

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
                        if terminalState == True:
                            print("Player " + str(GM.currentPlayer.noPlayer) +
                                  " win the game!")
                            running = False
                        GM.nextTurn()

        # Update
        pygame.display.update()