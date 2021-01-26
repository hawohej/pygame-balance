import pygame as pg
from time import time

from config import Config


class Score:
    """Класс, представляющий объект игрового счета.
    Формирование игрового счета происходит по следующей логике:
    Время, прошедшее с начала игры, умножается на 10 (для добавления первой цифры миллисекунд).
    Полученное значение приводится к типу int для сброса дробной части.

    Поля:

    - font - объект класса pygame.font.Font, представляющий шрифт для отображения игрового счета

    - value - численное значение игрового счета

    - start_time - время начала игры в секундах

    - image - объект класса pygame.Surface, представляющий изображение значения игрового счета

    - rect - объект pygame.Rect, представляющий прямоугольник для установки координат изображения
    игрового счета
    """
    def __init__(self, conf: Config):
        self.conf = conf

        self.font = pg.font.Font("resources/fonts/neuropolxrg.ttf", conf.score_font_size)
        self.value = 0
        self.start_time = None
        self.image = self.font.render(str(self.value), True, conf.score_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (conf.score_font_size, conf.score_font_size)

    def start(self):
        """Запуск таймера для вычисления значения игрового счета."""
        self.start_time = time()

    def update(self):
        """Обновление значения игрового счета."""
        current_time = time() - self.start_time
        self.value = str(int(current_time * 10))

    def prepare_image(self):
        """Обновление изображения в соответствии со значением игрового счета."""
        self.image = self.font.render(str(self.value), True, self.conf.score_color)

    def draw(self, surface: pg.Surface):
        """Отображение изображения игрового счета на передаваемой поверхности."""
        self.update()
        self.prepare_image()
        surface.blit(self.image, self.rect)
