import pygame
from pygame.sprite import Sprite


class Mob(Sprite):
    """Класс с игровым персонажем."""

    def __init__(self, my_game):
        Sprite.__init__(self)
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()

        # Создаем поверхность зеленого цвета и получаем прямоугольник
        self.image = pygame.image.load('mob.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана по середине
        self.rect.midtop = self.screen_rect.midtop

        # Сохранение вещественной координаты центра моба.
        self.x = float(self.rect.x)
        self.speedX = 5

    def update(self):
        """Обновляет позицию моба с учетом флага."""
        # Обновление атрибута x, не rect
        self.x += self.speedX
        if self.rect.left <= 0:
            self.speedX = 5
        if self.rect.right >= self.screen_rect.right:
            self.speedX = -5

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
