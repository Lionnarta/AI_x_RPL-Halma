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

def matriks_to_gui(matrik, setup):


# Main game screen
def main(x, screen):
    # Setup scale, x, y
    setup = base_setup(0,0,0)
    if(x == 8):
        setup.set_scale(85)
        setup.set_x(86)
        setup.set_y(44)
    if(x == 10):
        setup.set_scale(70)
        setup.set_x(81)
        setup.set_y(34)
    if(x == 16):
        setup.set_scale(45)
        setup.set_x(95)
        setup.set_y(24)

    # Loop running
    running = True
    # Game loop
    while running:
        screen.fill((53,50,50))
        evenodd = 0
        # Draw board to screen
        for i in range(1, x+1):
            for j in range(1, x+1):
                if evenodd % 2 == 0:
                    pygame.draw.rect(screen, (255,248,220), [setup.get_scale()*j+setup.get_x(), setup.get_scale()*i-setup.get_y(), setup.get_scale(), setup.get_scale()])
                else:
                    pygame.draw.rect(screen, (222,184,135), [setup.get_scale()*j+setup.get_x(), setup.get_scale()*i-setup.get_y(), setup.get_scale(), setup.get_scale()])
                evenodd += 1
            evenodd -= 1

        # Getter mouse coordinates -> Tuple X, Y
        mouse = pygame.mouse.get_pos()
        
        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if(setup.get_scale()+setup.get_x() <= mouse[0] <= setup.get_scale()*(x+1)+setup.get_x() and setup.get_scale()-setup.get_y() <= mouse[1] <= setup.get_scale()*(x+1)-setup.get_y()):
                    print(coordinate_to_point(mouse[0], mouse[1], setup))
        
        # Update
        pygame.display.update()