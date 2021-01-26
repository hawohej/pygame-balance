import pygame as pg
import math

from config import Config


class Player:
    """Класс, представляющий объекты игрока.

    Поля:

    - left и right задают движение модели игрока против и по часовой стрелке соответственно.

    - angle1 и angle2 указывают на угол, на котором находится каждый из объектов игрока.
    Расположение углов на окружности: 0 - восток, 90 - юг, 180 - запад, 270 - север.

    - rect1 и rect2 представление объектов игроков в виде квадратов. Используются для получения центров
    окружностей объектов игрока через центры квадратов. В ранней стадии разработки использовались для упрощения
    логики проверки на столкновения с блоками. После изменения метода collide_player в классе Block можно переписать
    в виде координат.
    """
    def __init__(self, conf: Config):
        self.conf = conf

        self.left = False
        self.right = False
        self.angle1 = 180
        self.angle2 = 0
        self.rect1 = pg.Rect((0, 0), (conf.player_width, conf.player_height))
        self.rect2 = pg.Rect((0, 0), (conf.player_width, conf.player_height))
        self.build()

    def build(self):
        """Устанавливает координаты для центров квадратов игрока."""
        self.rect1.center = (
            self.conf.circle_centerx - self.conf.circle_radius,
            self.conf.circle_centery
        )
        self.rect2.center = (
            self.conf.circle_centerx + self.conf.circle_radius,
            self.conf.circle_centery
        )

    def move(self):
        """В зависимости от значений left и right изменяет угол для квадратов игрока. После этого пересчитывает
        их координаты, используя радиус окружности, по которой двигаются квадраты и их углы.

        Формулы для рассчета координат:
        x = radius * cos(angle)
        y = radius * sin(angle)
        """
        if self.left:
            self.angle1 -= 2
            self.angle2 -= 2
        if self.right:
            self.angle1 += 2
            self.angle2 += 2

        self.rect1.center = (
            self.conf.circle_centerx + self.conf.circle_radius * math.cos(self.angle1 * math.pi / 180),
            self.conf.circle_centery + self.conf.circle_radius * math.sin(self.angle1 * math.pi / 180)
        )

        self.rect2.center = (
            self.conf.circle_centerx + self.conf.circle_radius * math.cos(self.angle2 * math.pi / 180),
            self.conf.circle_centery + self.conf.circle_radius * math.sin(self.angle2 * math.pi / 180)
        )

    def draw(self, surface: pg.Surface):
        """Отображение квадратов на передаваемой поверхности."""
        # Отображение окружности, по которой двигаются квадраты игрока
        # pg.draw.circle(
        #     surface,
        #     (200, 200, 200),
        #     (self.conf.player_centerx, self.conf.player_centery),
        #     self.conf.radius_between_players
        # )
        pg.draw.circle(
            surface,
            self.conf.player_color_1,
            self.rect1.center,
            self.conf.player_radius
        )
        pg.draw.circle(
            surface,
            self.conf.player_color_2,
            self.rect2.center,
            self.conf.player_radius
        )
        # Отображение квадратов игрока
        # Цвета игроков отражены для возможности отображения вместе с окружностями
        # pg.draw.rect(surface, self.conf.player_color_2, self.rect1)
        # pg.draw.rect(surface, self.conf.player_color_1, self.rect2)
