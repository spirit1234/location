# -*- coding:utf-8 -*-
import pygame
import sys


def test_key():
    """ 按键 ： 创建一个程序， 显示一个空屏幕。 在事件循环中， 每当检测到pygame.KEYDOWN 事件时都打印属性event.key 。 运行这个程序， 并按各种键， 看看
    Pygame如何响应。"""
    pygame.init()
    size = (1000, 600)
    bg_color = (255, 255, 255)
    text_color = (0, 0, 0)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('KEY TEST')
    font = pygame.font.Font('jjq.ttf', 25)
    text = font.render('', True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (500, 300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    screen.fill(bg_color)
                    screen.blit(font.render('up', True, text_color), text_rect)
                elif event.key == pygame.K_s:
                    screen.fill(bg_color)
                    screen.blit(font.render('down', True, text_color), text_rect)
                elif event.key == pygame.K_a:
                    screen.fill(bg_color)
                    screen.blit(font.render('left', True, text_color), text_rect)
                elif event.key == pygame.K_d:
                    screen.fill(bg_color)
                    screen.blit(font.render('right', True, text_color), text_rect)
            elif event.type == pygame.KEYUP:
                screen.fill(bg_color)
        pygame.display.flip()


test_key()
