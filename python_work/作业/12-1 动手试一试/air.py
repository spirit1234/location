# -*- coding:utf-8 -*-
""" 创建一个类， 将该角色绘制到屏幕中央， 并将该图像的背景色设置为屏幕背景色， 或将
屏幕背景色设置为该图像的背景色。"""
import pygame


class Air(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/air.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def describe(self):
        self.screen.blit(self.image, self.rect)
