# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        """在飞船位置创建子类对象"""
        super().__init__()
        self.screen = screen
        # 在(0,0)处创建子弹的矩形框
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        # 向上移动子弹，纵坐标值减少
        self.y -= self.speed_factor
        # 实时更新子弹的坐标
        self.rect.y = self.y

    def draw_bullet(self):
        # 在画布上创建子弹的矩形框
        pygame.draw.rect(self.screen, self.color, self.rect)
