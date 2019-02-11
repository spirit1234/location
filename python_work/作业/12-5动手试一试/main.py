# -*- coding:utf-8 -*-
import pygame
from air_set import Set
from airship import AirShip
import move_function as mf
from pygame.sprite import Group


def main_air():
    """侧面射击 ： 编写一个游戏， 将一艘飞船放在屏幕左边， 并允许玩家上下移动飞船。 在玩家按空格键时，
    让飞船发射一颗在屏幕中向右穿行的子弹， 并在子弹离开屏幕而消失后将其删除。"""
    pygame.init()
    air_set = Set()
    screen = pygame.display.set_mode((air_set.screen_width, air_set.screen_height))
    air_ship = AirShip(screen, air_set)
    pygame.display.set_caption('飞船')

    bullets = Group()
    while True:
        mf.check_airship_event(air_set, screen, air_ship, bullets)
        air_ship.air_ship_update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.right > air_ship.screen_rect.right:
                bullets.remove(bullet)
            print(len(bullets))
        mf.update_air_screen(air_set, screen, air_ship, bullets)


main_air()
