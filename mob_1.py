import pygame
from pygame.sprite import Sprite


class Mob_1(Sprite):
    """Класс с игровым персонажем."""

    def __init__(self, my_game):
        Sprite.__init__(self)
        self.screen = my_game.screen

        self.screen_rect = my_game.screen.get_rect()

        # Создаем поверхность зеленого цвета и получаем прямоугольник
        self.image = pygame.image.load('mob.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана по середине
        self.rect.midright = self.screen_rect.midright

        # Сохранение вещественной координаты центра корабля.
        self.y = float(self.rect.y)
        self.speedY = 5

    def update(self):
        """Обновляет позицию моба с учетом флага."""
        # Обновление атрибута x, не rect
        self.y += self.speedY
        if self.rect.top <= 0:
            self.speedY = 5
        if self.rect.bottom >= self.screen_rect.bottom:
            self.speedY = -5

        # Обновление атрибута rect на основании self.y
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)