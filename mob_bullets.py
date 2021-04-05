import pygame

import pygame

from pygame.sprite import Sprite


class Mob_bullet(Sprite):
    def __init__(self, my_game, x, y):
        Sprite.__init__(self)
        self.screen = my_game.screen
        self.life_player = my_game.life_player
        self.screen_rect = my_game.screen.get_rect()
        self.image = pygame.Surface((100, 10))
        self.image.fill((255, 0, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.mob_bullet_speed = -20

    def update(self):
        self.rect.y -= self.mob_bullet_speed
        # Убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
