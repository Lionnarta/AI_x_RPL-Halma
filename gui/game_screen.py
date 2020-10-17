import sys
import os
import pygame
import math
from pygame.locals import *


# Class to set shift x and y in game screen
class base_setup:
    def __init__(self, scale, x, y):
        self.scale = scale
        self.x = x
        self.y = y

    def get_scale(self):
        return self.scale

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_scale(self, scale):
        self.scale = scale

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


def coordinate_to_point(x, y, setup):
    x1 = (y + setup.get_y()) / setup.get_scale()
    y1 = (x - setup.get_x()) / setup.get_scale()
    return math.floor(x1), math.floor(y1)


# def matriks_to_list(matrik, setup):
#     list_pion = []
#     for i in range(matrik.size):
#         for j in range(matrik.size):
#             if matrik.cell.owner == 1:
#                 list_pion.append(((i+1,j+1),1))
#             elif matrik.cell.owner == 2:
#                 list_pion.append(((i+1,j+1),2))
#     return list_pion


# Main game screen
def main(x, screen):
    # Setup scale, x, y
    setup = base_setup(0, 0, 0)
    if (x == 8):
        setup.set_scale(85)
        setup.set_x(86)
        setup.set_y(44)
    if (x == 10):
        setup.set_scale(70)
        setup.set_x(81)
        setup.set_y(34)
    if (x == 16):
        setup.set_scale(45)
        setup.set_x(95)
        setup.set_y(24)

    list_pion = [((1, 1), 1), ((1, 2), 1), ((1, 3), 1), ((2, 1), 1),
                 ((2, 2), 1), ((3, 1), 1), ((8, 8), 2), ((8, 7), 2),
                 ((8, 6), 2), ((7, 7), 2), ((7, 8), 2), ((6, 8), 2)]
    # Loop running
    running = True
    # Game loop
    while running:
        screen.fill((53, 50, 50))
        evenodd = 0
        # Draw board to screen
        for i in range(1, x + 1):
            for j in range(1, x + 1):
                if evenodd % 2 == 0:
                    pygame.draw.rect(screen, (255, 248, 220), [
                        setup.get_scale() * j + setup.get_x(),
                        setup.get_scale() * i - setup.get_y(),
                        setup.get_scale(),
                        setup.get_scale()
                    ])
                else:
                    pygame.draw.rect(screen, (222, 184, 135), [
                        setup.get_scale() * j + setup.get_x(),
                        setup.get_scale() * i - setup.get_y(),
                        setup.get_scale(),
                        setup.get_scale()
                    ])
                evenodd += 1
            evenodd -= 1

        # Getter mouse coordinates -> Tuple X, Y
        mouse = pygame.mouse.get_pos()

        # List pion to gui
        for item in list_pion:
            if item[1] == 1:
                image = pygame.image.load(
                    os.path.join(os.path.dirname(os.getcwd()), "img",
                                 "collection", "green_pawn.png"))
                image = pygame.transform.scale(
                    image, (setup.get_scale(), setup.get_scale()))
                rect = image.get_rect()
                screen.blit(image,
                            (setup.get_scale() * item[0][1] + setup.get_x(),
                             setup.get_scale() * item[0][0] - setup.get_y()))
            elif item[1] == 2:
                image = pygame.image.load(
                    os.path.join(os.path.dirname(os.getcwd()), "img",
                                 "collection", "red_pawn.png"))
                image = pygame.transform.scale(
                    image, (setup.get_scale(), setup.get_scale()))
                rect = image.get_rect()
                screen.blit(image,
                            (setup.get_scale() * item[0][1] + setup.get_x(),
                             setup.get_scale() * item[0][0] - setup.get_y()))

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
                        setup.get_scale() * (x + 1) + setup.get_x()
                        and setup.get_scale() - setup.get_y() <= mouse[1] <=
                        setup.get_scale() * (x + 1) - setup.get_y()):
                    print(coordinate_to_point(mouse[0], mouse[1], setup))

        # Update
        pygame.display.update()