import sys
import os
import pygame
from pygame.locals import *
from game_screen import *

# Initialize the pygame
pygame.init()

# Set up display resolution
screen = pygame.display.set_mode((1024, 768))

# Title
pygame.display.set_caption("Halma")

# Icon
icon = pygame.image.load(
    os.path.join(os.path.dirname(os.getcwd()), "img", "icon", "halma.png"))
pygame.display.set_icon(icon)

# Getter width and height
width = screen.get_width()
height = screen.get_height()


# Procedure to start menu
def start():
    # Variable
    event_running = True
    active = 0
    board = 8
    player_default = 1
    txt = ''
    FONT = pygame.font.Font(None, 32)
    input_active = False
    # Game loop
    while event_running:
        # Screen background
        screen.fill((53, 50, 50))

        # Getter mouse coordinates -> Tuple X, Y
        mouse = pygame.mouse.get_pos()

        # Game mode
        game_mode = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "game_mode.png"))
        screen.blit(game_mode, (width / 2 - 425, height / 2 - 45))
        # Button game mode
        image_pvb_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "PvB_active.png"))
        image_pvb_a = pygame.transform.scale(image_pvb_a, (250, 100))
        image_pvb_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "PvB_unactive.png"))
        image_pvb_u = pygame.transform.scale(image_pvb_u, (250, 100))
        image_pvbl_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "PvBl_active.png"))
        image_pvbl_a = pygame.transform.scale(image_pvbl_a, (250, 100))
        image_pvbl_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "PvBl_unactive.png"))
        image_pvbl_u = pygame.transform.scale(image_pvbl_u, (250, 100))
        image_bvb_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "BvB_active.png"))
        image_bvb_a = pygame.transform.scale(image_bvb_a, (250, 100))
        image_bvb_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "BvB_unactive.png"))
        image_bvb_u = pygame.transform.scale(image_bvb_u, (250, 100))
        # Button game mode position
        pvb_position = Rect(width / 2 - 425, height / 2, 250, 100)
        pvbl_position = Rect(width / 2 - 125, height / 2, 250, 100)
        bvb_position = Rect(width / 2 + 175, height / 2, 250, 100)
        # Initiating screen blit
        if active == 0:
            screen.blit(image_pvb_a, pvb_position)
            screen.blit(image_pvbl_u, pvbl_position)
            screen.blit(image_bvb_u, bvb_position)
        if active == 1:
            screen.blit(image_pvb_u, pvb_position)
            screen.blit(image_pvbl_a, pvbl_position)
            screen.blit(image_bvb_u, bvb_position)
        if active == 2:
            screen.blit(image_pvb_u, pvb_position)
            screen.blit(image_pvbl_u, pvbl_position)
            screen.blit(image_bvb_a, bvb_position)

        # Board size
        board_size = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "board_size.png"))
        screen.blit(board_size, (width / 2 - 425, height / 2 + 120))
        # Button board size
        eight_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "eight_a.png"))
        eight_a = pygame.transform.scale(eight_a, (100, 30))
        eight_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "eight_u.png"))
        eight_u = pygame.transform.scale(eight_u, (100, 30))
        ten_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "ten_a.png"))
        ten_a = pygame.transform.scale(ten_a, (100, 30))
        ten_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "ten_u.png"))
        ten_u = pygame.transform.scale(ten_u, (100, 30))
        sixteen_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "sixteen_a.png"))
        sixteen_a = pygame.transform.scale(sixteen_a, (100, 30))
        sixteen_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "sixteen_u.png"))
        sixteen_u = pygame.transform.scale(sixteen_u, (100, 30))
        # Button board size position
        eight_pos = Rect(width / 2 - 425, height / 2 + 160, 100, 30)
        ten_pos = Rect(width / 2 - 225, height / 2 + 160, 100, 30)
        sixteen_pos = Rect(width / 2 - 25, height / 2 + 160, 100, 30)
        # Initiating screen blit
        if board == 8:
            screen.blit(eight_a, eight_pos)
            screen.blit(ten_u, ten_pos)
            screen.blit(sixteen_u, sixteen_pos)
        if board == 10:
            screen.blit(eight_u, eight_pos)
            screen.blit(ten_a, ten_pos)
            screen.blit(sixteen_u, sixteen_pos)
        if board == 16:
            screen.blit(eight_u, eight_pos)
            screen.blit(ten_u, ten_pos)
            screen.blit(sixteen_a, sixteen_pos)

        # Time box
        time_limit = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "time_limit.png"))
        screen.blit(time_limit, (width / 2 - 425, height / 2 + 210))
        time_box_pos = Rect(width / 2 - 265, height / 2 + 210, 45, 26)
        if not input_active:
            txt_pos = FONT.render(txt, True, Color('#A4A4A4'))
        else:
            txt_pos = FONT.render(txt, True, Color('white'))
        screen.blit(txt_pos, time_box_pos)
        if input_active:
            time_box = pygame.image.load(
                os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                             "time_box_a.png"))
            screen.blit(time_box, (width / 2 - 265, height / 2 + 210))
        else:
            time_box = pygame.image.load(
                os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                             "time_box_u.png"))
            screen.blit(time_box, (width / 2 - 265, height / 2 + 210))

        # Player
        player = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "player.png"))
        if active == 0 or active == 1:
            screen.blit(player, (width / 2 - 425, height / 2 + 265))
        # Player color selection
        green_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "green_a.png"))
        green_a = pygame.transform.scale(green_a, (60, 60))
        green_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "green_u.png"))
        green_u = pygame.transform.scale(green_u, (60, 60))
        red_a = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "red_a.png"))
        red_a = pygame.transform.scale(red_a, (60, 60))
        red_u = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "red_u.png"))
        red_u = pygame.transform.scale(red_u, (60, 60))
        # Player pos
        green_pos = Rect(width / 2 - 265, height / 2 + 265, 60, 60)
        red_pos = Rect(width / 2 - 180, height / 2 + 265, 60, 60)
        # Initiating player
        if player_default == 1 and (active == 0 or active == 1):
            screen.blit(green_a, green_pos)
            screen.blit(red_u, red_pos)
        elif player_default == 2 and (active == 0 or active == 1):
            screen.blit(green_u, green_pos)
            screen.blit(red_a, red_pos)

        # Play button
        play = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "play.png"))
        play = pygame.transform.scale(play, (120, 60))
        play_h = pygame.image.load(
            os.path.join(os.path.dirname(os.getcwd()), "img", "collection",
                         "play_h.png"))
        play_h = pygame.transform.scale(play_h, (120, 60))
        # Play pos
        play_pos = Rect(width / 2 + width / 4, height / 2 + 300, 120, 60)
        # show play
        if (width / 2 + width / 4 <= mouse[0] <= width / 2 + width / 4 +
                120) and (height / 2 + 300 <= mouse[1] <= height / 2 + 360):
            screen.blit(play_h, play_pos)
        else:
            screen.blit(play, play_pos)

        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                event_running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if input_active:
                    if event.key == K_0 or event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9:
                        txt += event.unicode
                    if event.key == K_BACKSPACE:
                        txt = txt[:-1]
                    txt_pos = FONT.render(txt, True, Color('white'))
            # check if button clicked
            if event.type == MOUSEBUTTONDOWN:
                # game mode
                if (pvb_position.collidepoint(mouse[0],
                                              mouse[1])) and (active != 0):
                    screen.blit(image_pvb_a, pvb_position)
                    screen.blit(image_pvbl_u, pvbl_position)
                    screen.blit(image_bvb_u, bvb_position)
                    active = 0
                if (pvbl_position.collidepoint(mouse[0],
                                               mouse[1])) and (active != 1):
                    screen.blit(image_pvb_u, pvb_position)
                    screen.blit(image_pvbl_a, pvbl_position)
                    screen.blit(image_bvb_u, bvb_position)
                    active = 1
                if (bvb_position.collidepoint(mouse[0],
                                              mouse[1])) and (active != 2):
                    screen.blit(image_pvb_u, pvb_position)
                    screen.blit(image_pvbl_u, pvbl_position)
                    screen.blit(image_bvb_a, bvb_position)
                    active = 2
                # board size
                if (eight_pos.collidepoint(mouse[0],
                                           mouse[1])) and (board != 8):
                    screen.blit(eight_a, eight_pos)
                    screen.blit(ten_u, ten_pos)
                    screen.blit(sixteen_u, sixteen_pos)
                    board = 8
                if (ten_pos.collidepoint(mouse[0],
                                         mouse[1])) and (board != 10):
                    screen.blit(eight_u, eight_pos)
                    screen.blit(ten_a, ten_pos)
                    screen.blit(sixteen_u, sixteen_pos)
                    board = 10
                if (sixteen_pos.collidepoint(mouse[0],
                                             mouse[1])) and (board != 16):
                    screen.blit(eight_u, eight_pos)
                    screen.blit(ten_u, ten_pos)
                    screen.blit(sixteen_a, sixteen_pos)
                    board = 16
                # time box
                if (time_box_pos.collidepoint(mouse[0], mouse[1])):
                    input_active = True
                else:
                    input_active = False
                # player
                if (green_pos.collidepoint(mouse[0], mouse[1])
                    ) and player_default == 2 and (active == 0 or active == 1):
                    screen.blit(green_a, green_pos)
                    screen.blit(red_u, red_pos)
                    player_default = 1
                if (red_pos.collidepoint(mouse[0], mouse[1])
                    ) and player_default == 1 and (active == 0 or active == 1):
                    screen.blit(green_u, green_pos)
                    screen.blit(red_a, red_pos)
                    player_default = 2
                # Play
                if (play_pos.collidepoint(mouse[0], mouse[1])):
                    if txt == '':
                        main(screen, active, board, player_default, '20')
                    elif active == 2:
                        main(screen, active, board, 0, txt)
                    else:
                        main(screen, active, board, player_default, txt)

        # Update display
        pygame.display.update()


# start game
start()

pygame.quit()
sys.exit()
