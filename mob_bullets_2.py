import pygame

from pygame.sprite import Sprite


class Mob_bullet_2(Sprite):
    def __init__(self, my_game, x, y):
        Sprite.__init__(self)
        self.screen = my_game.screen

        self.screen_rect = my_game.screen.get_rect()
        self.image = pygame.Surface((10, 100))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.midleft = x
        self.rect.midleft = y
        self.mob_bullet_speed = 15

    def update(self):
        self.rect.x += self.mob_bullet_speed
        # Убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom > self.screen_rect.right:
            self.kill()