# -*- coding:utf-8 -*-
import sys
import pygame


def check_keydown(event, rocket):
    if event.key == pygame.K_w:
        rocket.move_up = True
    elif event.key == pygame.K_s:
        rocket.move_down = True
    elif event.key == pygame.K_a:
        rocket.move_left = True
    elif event.key == pygame.K_d:
        rocket.move_right = True


def check_keyup(event, rocket):
    if event.key == pygame.K_w:
        rocket.move_up = False
    elif event.key == pygame.K_s:
        rocket.move_down = False
    elif event.key == pygame.K_a:
        rocket.move_left = False
    elif event.key == pygame.K_d:
        rocket.move_right = False


def check_rocket_event(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup(event, rocket)


def update_rocket_screen(def_set, rocket, screen):
    screen.fill(def_set.bg_color)
    rocket.blit()
    pygame.display.flip()
