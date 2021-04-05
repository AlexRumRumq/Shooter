import pygame

from pygame.sprite import Sprite


class Bullet_3(Sprite):
    def __init__(self, my_game, x, y):
        Sprite.__init__(self)
        self.screen = my_game.screen

        self.screen_rect = my_game.screen.get_rect()
        self.image = pygame.Surface((50, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.midright = x
        self.rect.midright = y
        self.bullet_speed = -15

    def update(self):
        self.rect.x += self.bullet_speed
        # Убить, если он заходит за верхнюю часть экрана
        if self.rect.right < 0:
            self.kill()