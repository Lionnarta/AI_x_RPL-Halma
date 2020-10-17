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
icon = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "icon", "halma.png"))
pygame.display.set_icon(icon)

# Getter width and height
width = screen.get_width()
height = screen.get_height()

# Procedure to start menu
def start():
    # Variable
    event_running = True
    active = 1
    board = 8
    # Game loop
    while event_running:
        # Screen background
        screen.fill((53, 50, 50))

        # Getter mouse coordinates -> Tuple X, Y
        mouse = pygame.mouse.get_pos()

        # Game mode
        game_mode = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "game_mode.png"))
        screen.blit(game_mode, (width/2-275, height/2-45))
        # Button game mode
        image_pvb_a = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "PvB_active.png"))
        image_pvb_a = pygame.transform.scale(image_pvb_a, (250, 100))
        image_pvb_u = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "PvB_unactive.png"))
        image_pvb_u = pygame.transform.scale(image_pvb_u, (250, 100))
        image_bvb_a = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "BvB_active.png"))
        image_bvb_a = pygame.transform.scale(image_bvb_a, (250, 100))
        image_bvb_u = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "BvB_unactive.png"))
        image_bvb_u = pygame.transform.scale(image_bvb_u, (250, 100))
        # Button game mode position
        pvb_position = Rect(width/2-275, height/2, 250, 100)
        bvb_position = Rect(width/2+25, height/2, 250, 100)
        # Initiating screen blit
        if active == 1:
            screen.blit(image_pvb_a, pvb_position)
            screen.blit(image_bvb_u, bvb_position)
        if active == 0:
            screen.blit(image_pvb_u, pvb_position)
            screen.blit(image_bvb_a, bvb_position)

        # Board size
        board_size = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "board_size.png"))
        screen.blit(board_size, (width/2-275, height/2+120))
        # Button board size
        eight_a = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "eight_a.png"))
        eight_a = pygame.transform.scale(eight_a, (100, 30))
        eight_u = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "eight_u.png"))
        eight_u = pygame.transform.scale(eight_u, (100, 30))
        ten_a = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "ten_a.png"))
        ten_a = pygame.transform.scale(ten_a, (100, 30))
        ten_u = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "ten_u.png"))
        ten_u = pygame.transform.scale(ten_u, (100, 30))
        sixteen_a = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "sixteen_a.png"))
        sixteen_a = pygame.transform.scale(sixteen_a, (100, 30))
        sixteen_u = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()), "img", "collection", "sixteen_u.png"))
        sixteen_u = pygame.transform.scale(sixteen_u, (100, 30))
        # Button board size position
        eight_pos = Rect(width/2-275, height/2+160, 100, 30)
        ten_pos = Rect(width/2-75, height/2+160, 100, 30)
        sixteen_pos = Rect(width/2+125, height/2+160, 100, 30)
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

        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                event_running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # check if button clicked
            if event.type == MOUSEBUTTONDOWN:
                if(pvb_position.collidepoint(mouse[0], mouse[1])) and (active == 0):
                    screen.blit(image_pvb_a, pvb_position)
                    screen.blit(image_bvb_u, bvb_position)
                    active = 1
                if(bvb_position.collidepoint(mouse[0], mouse[1])) and (active == 1):
                    screen.blit(image_pvb_u, pvb_position)
                    screen.blit(image_bvb_a, bvb_position)
                    active = 0
                if(eight_pos.collidepoint(mouse[0], mouse[1])) and (board != 8):
                    screen.blit(eight_a, eight_pos)
                    screen.blit(ten_u, ten_pos)
                    screen.blit(sixteen_u, sixteen_pos)
                    board = 8
                if(ten_pos.collidepoint(mouse[0], mouse[1])) and (board != 10):
                    screen.blit(eight_u, eight_pos)
                    screen.blit(ten_a, ten_pos)
                    screen.blit(sixteen_u, sixteen_pos)
                    board = 10
                if(sixteen_pos.collidepoint(mouse[0], mouse[1])) and (board != 16):
                    screen.blit(eight_u, eight_pos)
                    screen.blit(ten_u, ten_pos)
                    screen.blit(sixteen_a, sixteen_pos)
                    board = 16
                
        # # Button event
        # if button_1.collidepoint(mouse[0], mouse[1]):
        #     if click:
        #         main(8, screen)
        # if button_2.collidepoint(mouse[0], mouse[1]):
        #     if click:
        #         main(10, screen)
        # if button_3.collidepoint(mouse[0], mouse[1]):
        #     if click:
        #         main(16, screen)     

        # Update display
        pygame.display.update()


# start game
start()

pygame.quit()
sys.exit()
