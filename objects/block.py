import pygame as pg
from random import randint
import math

from config import Config

from objects.player import Player


class Block(pg.Rect):
    """Класс, представляющий объект блока.

    Поля:

    - speed - смещение блока вниз при вызове метода drop (в пикселях)
    """
    def __init__(self, conf: Config):
        self.conf = conf

        super(Block, self).__init__((0, 0), (0, 0))

        self.speed = 2
        self.build()

    def build(self):
        """Установка координат и размеров блока в зависимости от типа.
        Тип блока определяется случайно.
        """
        block_type = randint(1, 3)

        if block_type == 1:
            self.width = (self.conf.window_width // 2 - self.conf.window_width // 3) * 2
            self.centerx = self.conf.window_width // 3
        elif block_type == 2:
            self.width = (self.conf.window_width // 3 * 2 - self.conf.window_width // 2) * 2
            self.centerx = self.conf.window_width // 3 * 2
        elif block_type == 3:
            self.width = self.conf.circle_radius - self.conf.player_radius
            self.centerx = self.conf.window_width // 2
            self.speed = 3

        self.height = self.conf.circle_radius // 2
        self.bottom = 0

    def collide_player(self, player: Player) -> bool:
        """Проверка столкновения блока с объектом игрока.
        Старый вариант проверяет столкновение через квадраты игрока.
        Новый вариант рассчитывает координаты точек окружности игрока и
        проверяется соприкосновение блока с каждой из них.

        Формула рассчета координат точек аналогична формуле для рассчета координат
        объектов игроков в методе move класса Player.
        """
        # Старый вариант проверки столкновения через квадраты игрока
        # return self.colliderect(player.rect1) or self.colliderect(player.rect2)
        for angle in range(360):
            if self.collidepoint(
                player.rect1.centerx + self.conf.player_radius * math.cos(angle * math.pi / 180),
                player.rect1.centery + self.conf.player_radius * math.sin(angle * math.pi / 180)
            ) or self.collidepoint(
                player.rect2.centerx + self.conf.player_radius * math.cos(angle * math.pi / 180),
                player.rect2.centery + self.conf.player_radius * math.sin(angle * math.pi / 180)
            ):
                return True
        return False

    def drop(self):
        """Перемещение блока на speed пикселей вниз."""
        self.move_ip(0, self.speed)

    def draw(self, surface: pg.Surface):
        """Отображение блока на передаваемой поверхности."""
        pg.draw.rect(surface, self.conf.block_color, self)
