# -*- coding:utf-8 -*-
"""创建一个背景为蓝色的Pygame窗口。"""
import pygame
from air import Air
from general_settings import Set
import game_function as info


def run_sky():
    pygame.init()
    general = Set()
    screen = pygame.display.set_mode(general.size)
    air = Air(screen)
    pygame.display.set_caption('Blue Sky')
    while True:
        info.check_event()
        info.update(general, air, screen)


run_sky()
