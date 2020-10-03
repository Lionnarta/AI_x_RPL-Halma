import sys
import os
import pygame
from pygame.locals import *

def main(x, screen):
    running = True
    while running:
        screen.fill((53,50,50))
        evenodd = 0
        if x == 8:
            for i in range(1, x+1):
                for j in range(1, x+1):
                    if evenodd % 2 == 0:
                        pygame.draw.rect(screen, (255,248,220), [85*j+86, 85*i-44, 85, 85])
                    else:
                        pygame.draw.rect(screen, (222,184,135), [85*j+86, 85*i-44, 85, 85])
                    evenodd += 1
                evenodd -= 1
        if x == 10:
            for i in range(1, x+1):
                for j in range(1, x+1):
                    if evenodd % 2 == 0:
                        pygame.draw.rect(screen, (255,248,220), [70*j+81, 70*i-34, 70, 70])
                    else:
                        pygame.draw.rect(screen, (222,184,135), [70*j+81, 70*i-34, 70, 70])
                    evenodd += 1
                evenodd -= 1
        if x == 16:
            for i in range(1, x+1):
                for j in range(1, x+1):
                    if evenodd % 2 == 0:
                        pygame.draw.rect(screen, (255,248,220), [45*j+95, 45*i-24, 45, 45])
                    else:
                        pygame.draw.rect(screen, (222,184,135), [45*j+95, 45*i-24, 45, 45])
                    evenodd += 1
                evenodd -= 1

        # Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        # Update
        pygame.display.update()