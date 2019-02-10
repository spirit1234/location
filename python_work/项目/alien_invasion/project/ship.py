# -*- coding:utf-8 -*-
import pygame
from bullet import Bullet

class Ship(object):
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        # 获取飞船的矩形框
        self.rect = self.image.get_rect()
        # 获取屏幕的矩形框
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船的坐标与屏幕的对齐
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.bottom)
        self.moving_right = self.moving_left = self.moving_up = self.moving_down = self.moving_bullet =False

    def update(self,  ai_settings, screen, ship, bullets):
        """根据移动标志调整飞船位置"""
        # if self.moving_right:
        #     self.center += self.ai_settings.ship_speed_factor
        #
        # if self.moving_left:
        #     self.center -= self.ai_settings.ship_speed_factor
        # 防止出右侧边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # 防止出左侧边界
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center1 -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center1 += self.ai_settings.ship_speed_factor
        if self.moving_bullet:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.center1

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)
