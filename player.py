import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    """Класс с игровым персонажем."""

    def __init__(self, my_game):
        Sprite.__init__(self)
        self.screen = my_game.screen

        self.screen_rect = my_game.screen.get_rect()

        # Создаем поверхность зеленого цвета и получаем прямоугольник
        self.image = pygame.image.load('image_player.jpg')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.image.set_alpha(500)
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана по середине
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.player_speed = 12
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию игрока с учетом флага."""
        # Обновление атрибута x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.player_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)