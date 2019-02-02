import sys
import pygame


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update(general, air, screen):
    screen.fill(general.bg_color)
    air.describe()
    pygame.display.flip()
