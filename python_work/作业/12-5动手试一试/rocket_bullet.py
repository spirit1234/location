import pygame
from pygame.sprite import Sprite


class RocketBullet(Sprite):
    def __init__(self, air_set, screen, air_ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, air_set.bullet_w, air_set.bullet_h)
        self.rect.right = air_ship.screen_rect.centerx
        self.rect.centery = air_ship.rect.centery
        self.x = float(self.rect.x)
        self.color = air_set.bullet_set_color
        self.speed = air_set.bullet_set_speed

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw_air_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
