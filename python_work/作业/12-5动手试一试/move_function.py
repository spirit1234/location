import sys
import pygame
from rocket_bullet import RocketBullet


def check_keydown(event, air_set, screen, air_ship, bullets):
    if event.key == pygame.K_w:
        air_ship.move_up = True
    elif event.key == pygame.K_s:
        air_ship.move_down = True
    elif event.key == pygame.K_SPACE:
        new_bullets = RocketBullet(air_set, screen, air_ship)
        bullets.add(new_bullets)


def check_keyup(event, air_ship):
    if event.key == pygame.K_w:
        air_ship.move_up = False
    elif event.key == pygame.K_s:
        air_ship.move_down = False


def check_airship_event(air_set, screen, air_ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, air_set, screen, air_ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, air_ship)


def update_air_screen(air_set, screen, air_ship, bullets):
    screen.fill(air_set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_air_bullet()
    air_ship.blit_it()
    pygame.display.flip()
