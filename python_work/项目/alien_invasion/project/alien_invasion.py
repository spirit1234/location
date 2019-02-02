import pygame
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化游戏并创建对象"""
    pygame.init()
    ai_settings = Settings()
    size = (ai_settings.screen_width, ai_settings.screen_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()
