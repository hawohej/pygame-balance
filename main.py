import pygame as pg

from config import Config

from layers.game import Game


def run():
    # Инициализация pygame и компонентов
    pg.init()
    pg.display.init()
    pg.display.set_caption("Balance")

    conf = Config()  # Создание объекта конфигурации
    screen = pg.display.set_mode((conf.window_width, conf.window_height))  # Создание поверхности экрана

    Game(conf, screen).start()  # Создание и запуск объекта игры


if __name__ == '__main__':
    run()
