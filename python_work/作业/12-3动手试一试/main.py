import pygame
from set import Set
from rocket import Rocket
import rocket_function
"""编写一个游戏，开始时屏幕中央有一个火箭，而玩家可使用四个方向键上下左右移动火箭。请务必确保火箭不会移到屏幕外面。"""


def run_game():
    pygame.display.init()
    def_set = Set()
    screen = pygame.display.set_mode((def_set.width, def_set.height))
    pygame.display.set_caption('Rocket')
    rocket = Rocket(def_set, screen)
    while True:
        rocket_function.check_rocket_event(rocket)
        rocket.moving()
        rocket_function.update_rocket_screen(def_set, rocket, screen)


run_game()
