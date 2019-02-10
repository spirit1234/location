# -*- coding:utf-8 -*-
class Settings(object):
    """存储设置类"""

    def __init__(self):
        # 屏幕尺寸设置
        self.screen_width = 1200
        self.screen_height = 600
        # 屏幕背景色
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed_factor = 1.5
        # 子弹速度
        self.bullet_speed_factor = 1
        # 子弹矩形框尺寸
        self.bullet_width = 3
        self.bullet_height = 15
        # 子弹颜色
        self.bullet_color = 60, 60, 60
        