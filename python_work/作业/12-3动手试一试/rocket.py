# -*- coding:utf-8 -*-
import pygame


class Rocket(object):
    def __init__(self, setting, screen):
        self.screen = screen
        self.set = setting
        self.image = pygame.image.load('img/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def moving(self):
        if self.move_up and self.rect.top > 0:
            self.center_vertical -= self.set.set_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_vertical += self.set.set_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center_horizontal += self.set.set_speed
        if self.move_left and self.rect.left > 0:
            self.center_horizontal -= self.set.set_speed
        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical

    def blit(self):
        self.screen.blit(self.image, self.rect)
