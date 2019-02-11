import pygame


class AirShip(object):
    def __init__(self, screen, air_set):
        self.screen = screen
        self.air_set = air_set
        self.img = pygame.image.load('img/rocket.bmp')
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.centery = float(self.rect.centery)

        self.move_up = self.move_down = False

    def air_ship_update(self):
        if self.move_up and self.rect.top > 0:
            self.centery -= self.air_set.air_speed
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.air_set.air_speed

        self.rect.centery = self.centery

    def blit_it(self):
        self.screen.blit(self.img, self.rect)
