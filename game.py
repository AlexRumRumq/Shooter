import sys

import pygame
import random

from mob import Mob
from mob_1 import Mob_1
from mob_2 import Mob_2
from player import Player
from bullet import Bullet
from bullet_2 import Bullet_2
from bullet_3 import Bullet_3
from mob_bullets import Mob_bullet
from mob_bullets_1 import Mob_bullet_1
from mob_bullets_2 import Mob_bullet_2


class Game:

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('игра топ 1')
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.BLACK = (0, 0, 0)

        self.sound1 = pygame.mixer.Sound('shoot.wav')
        self.sound2 = pygame.mixer.Sound('shoot_in_player.wav')

        # Создание экземпляра игрока
        self.player = Player(self)

        # Создание экземпляра mob и добавление его в группу mobs.
        # Группа нужна для того, чтобы мы могли удалить его в случае потери всех жизней.
        self.mob = Mob(self)
        self.mobs = pygame.sprite.Group()
        self.mobs.add(self.mob)

        # Создание экземпляра mob_1 и добавление его в группу mobs_1.
        # Группа нужна для того, чтобы мы могли удалить его в случае потери всех жизней.
        self.mob_1 = Mob_1(self)
        self.mobs_1 = pygame.sprite.Group()
        self.mobs_1.add(self.mob_1)

        # Создание экземпляра mob_2 и добавление его в группу mobs_2.
        # Группа нужна для того, чтобы мы могли удалить его в случае потери всех жизней.
        self.mob_2 = Mob_2(self)
        self.mobs_2 = pygame.sprite.Group()
        self.mobs_2.add(self.mob_2)

        # Создание группы для снарядов игрока и снарядов мобов.
        self.bullets = pygame.sprite.Group()
        self.mob_bullets = pygame.sprite.Group()

        # Жизни игрока, жизни всех мобов.
        self.life_player = 50
        self.life_mob = 75
        self.life_mob_1 = 50
        self.life_mob_2 = 50

        # Переменная для создания игрового цикла
        # Используем не sys.exit(), потому что нам нужно показать, кто победил.
        self.running = True

    def shoot(self):
        """Метод для стрельбы игрока вверх."""
        bullet = Bullet(self, self.player.rect.centerx, self.player.rect.top)
        self.bullets.add(bullet)

    def shoot_2(self):
        """Метод для стрельбы игрока вправо."""
        bullet_2 = Bullet_2(self, self.player.rect.midright, self.player.rect.midright)
        self.bullets.add(bullet_2)

    def shoot_3(self):
        """Метод для стрельбы игрока влево."""
        bullet_3 = Bullet_3(self, self.player.rect.midleft, self.player.rect.midleft)
        self.bullets.add(bullet_3)

    def shoot_mob(self):
        """Метод для стрельбы моба."""
        mob_bullet = Mob_bullet(self, self.mob.rect.centerx, self.mob.rect.bottom)
        self.mob_bullets.add(mob_bullet)

    def shoot_mob_1(self):
        """Метод для стрельбы моба_1."""
        mob_bullet_1 = Mob_bullet_1(self, self.mob_1.rect.midleft, self.mob_1.rect.midleft)
        self.mob_bullets.add(mob_bullet_1)

    def shoot_mob_2(self):
        """Метод для стрельбы моба_2."""
        mob_bullet_2 = Mob_bullet_2(self, self.mob_2.rect.midright, self.mob_2.rect.midright)
        self.mob_bullets.add(mob_bullet_2)

    def our_life(self):
        """Метод для отображения количества жизней."""
        # Жизни игрока
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'{self.life_player}', True,
                          (150, 0, 150))
        self.screen.blit(text1, (self.screen.get_rect().width / 2,
                                 self.screen.get_rect().height - 50))

        # Жизни моба
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'{self.life_mob}', True,
                          (180, 0, 0))
        self.screen.blit(text1, (self.screen.get_rect().width / 2, 20))

        # Жизни моба_1
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'{self.life_mob_1}', True,
                          (180, 0, 0))
        self.screen.blit(text1, (self.screen.get_rect().width - 50, 20))

        # Жизни моба_2
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'{self.life_mob_2}', True,
                          (180, 0, 0))
        self.screen.blit(text1, (14, 20))

    def end_game(self):
        """Метод для вывода на экран после завершения игры фразы "Игра окончена!!!" """
        self.screen.fill(self.BLACK)
        f1 = pygame.font.Font(None, 150)
        text1 = f1.render('ИГРА ОКОНЧЕНА!!!', True,
                          (0, 255, 0))
        self.screen.blit(text1, (self.screen.get_rect().width / 2 - 500,
                                 self.screen.get_rect().height / 2 - 50))
        pygame.display.flip()
        # Задержка надписи на 25000 милисекунд
        pygame.time.delay(2500)

    def win_game(self):
        """Метод для вывода на экран после завершения игры фразы "Ты победил!!!" """
        self.screen.fill(self.BLACK)
        f1 = pygame.font.Font(None, 150)
        text1 = f1.render('Ты победил!!!', True,
                          (40, 120, 255))
        self.screen.blit(text1, (self.screen.get_rect().width / 2 - 350,
                                 self.screen.get_rect().height / 2 - 50))
        pygame.display.flip()
        # Задержка надписи на 2500 милисекунд
        pygame.time.delay(2500)

    def update_screen(self):
        """Метод для всех обновлений и отрисовок всех элементов"""
        self.player.update()
        self.bullets.update()

        self.mobs.update()
        self.mobs_1.update()
        self.mobs_2.update()

        self.mob_bullets.update()

        # Обработка столкновений

        # столкновение игрока и снарядов мобов с последующим удалением снаряда(так как указано True)
        hits_1 = pygame.sprite.spritecollide(self.player, self.mob_bullets, True)

        # столкновение моба, моба_1, моба_2 и снарядов игрока с последующим удалением снаряда(так как указано True)
        # False показывает, что удалять моба не нужно
        hits_2 = pygame.sprite.groupcollide(self.mobs, self.bullets, False, True)
        hits_3 = pygame.sprite.groupcollide(self.mobs_1, self.bullets, False, True)
        hits_4 = pygame.sprite.groupcollide(self.mobs_2, self.bullets, False, True)

        # столкновение игрока и моба. Игра окончена.
        hits_5 = pygame.sprite.spritecollide(self.player, self.mobs, True)
        hits_6 = pygame.sprite.spritecollide(self.player, self.mobs_1, True)
        hits_7 = pygame.sprite.spritecollide(self.player, self.mobs_2, True)

        hits_8 = pygame.sprite.groupcollide(self.mobs_1, self.mob_bullets, False, True)
        hits_9 = pygame.sprite.groupcollide(self.mobs_2, self.mob_bullets, False, True)

        # проверка было ли столкновение hits_1
        # если было, то вычитаем жизнь, и если жизней 0, то
        # выходим из цикла с помощью self.running = False
        # и вызываем метод отрисовки надписи "Игра окончена!!!"
        if hits_1:
            self.sound2.play()
            self.life_player -= 1
            if self.life_player == 0:
                self.running = False
                self.end_game()

        # проверка было ли столкновение hits_2, hits_3, hits_4
        # если было, то вычитаем жизнь, и если жизней 0, то
        # удаляем моба
        if hits_2:
            self.life_mob -= 1
            if self.life_mob <= 0:
                self.mob.kill()
        if hits_3:
            self.life_mob_1 -= 1
            if self.life_mob_1 <= 0:
                self.mob_1.kill()
        if hits_4:
            self.life_mob_2 -= 1
            if self.life_mob_2 <= 0:
                self.mob_2.kill()

        # Если игрок коснулся моба, моба_1 или моба_2, то игра заканчивается
        # Выскакивает надпись "Игра окончена!!!"
        if hits_5 or hits_6 or hits_7:
            self.running = False
            game.end_game()

        # Если все мобы убиты, то игра заканчивается и выскакивает надпись "Ты победил!!!"
        if self.life_mob <= 0 and self.life_mob_1 <= 0 and self.life_mob_2 <= 0:
            self.running = False
            self.win_game()

        # Если моб 1 попадает в моб 2 и наоборот - то
        # жизни моба, в которог попали увеличатся на 1
        if hits_8:
            self.life_mob_1 += 1

        if hits_9:
            self.life_mob_2 += 1

        self.screen.fill(self.BLACK)
        self.bullets.draw(self.screen)
        self.mob_bullets.draw(self.screen)
        self.player.blitme()

        self.mobs.draw(self.screen)
        self.mobs_1.draw(self.screen)
        self.mobs_2.draw(self.screen)
        self.our_life()
        pygame.display.flip()

    def run_game(self):
        """Игровой цикл"""
        while self.running:
            # Цикл с определенным FPSa
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.player.moving_right = True
                    if event.key == pygame.K_a:
                        self.player.moving_left = True
                    elif event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_w:
                        self.player.moving_up = True
                    if event.key == pygame.K_s:
                        self.player.moving_down = True
                    if event.key == pygame.K_SPACE:
                        self.sound1.play()
                        self.shoot()
                        self.shoot_2()
                        self.shoot_3()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.moving_right = False
                    if event.key == pygame.K_a:
                        self.player.moving_left = False
                    if event.key == pygame.K_s:
                        self.player.moving_down = False
                    if event.key == pygame.K_w:
                        self.player.moving_up = False
            z = random.randint(0, 1000)
            if self.life_mob > 0 and z % 50 == 0:
                self.shoot_mob()
            if self.life_mob_1 > 0 and z % 100 == 0:
                self.shoot_mob_1()
            if self.life_mob_2 > 0 and z % 100 == 0:
                self.shoot_mob_2()
            self.update_screen()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    game = Game()
    game.run_game()
