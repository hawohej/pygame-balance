import pygame as pg
import sys
import time

from config import Config

from objects.player import Player
from objects.block import Block
from objects.score import Score


class Game:
    """Класс, представляющий игру.

    Поля:

    - player - объект класса Player, представляющий игрока

    - blocks - список объектов класса Block, представляющий блоки

    - score - объект класса Score, представляющий игровой счёт

    - clock - объект pygame.time.Clock для задания количества
    выполнений основного игрового цикла в секунду
    """
    def __init__(self, conf: Config, screen: pg.Surface):
        self.conf = conf
        self.screen = screen

        self.player = Player(conf)
        self.blocks = list()
        self.score = Score(conf)
        self.clock = pg.time.Clock()

    def generate_block(self):
        """Создает и добавляет новый блок в список блоков."""
        self.blocks.append(Block(self.conf))

    def start(self):
        # Добавление первого блока в список
        self.generate_block()
        # Запуск ведения игрового счета
        self.score.start()
        while True:
            self.get_input()
            self.player.move()
            self.move_blocks()
            self.update_screen()

    def move_blocks(self):
        """Перемещение каждого блока из списка вниз. Проверяются условия
        для создания, удаления и столкновения блоков с игроком.
        """
        for block in self.blocks:
            block.drop()

            # Проверка необходимости создания нового блока
            if block.top >= self.conf.window_height // 2 and len(self.blocks) < 2:
                self.generate_block()
            # Проверка необходимости удаления блока
            if block.top >= self.conf.window_height:
                self.blocks.remove(block)
            # Проверка столкновения блока с игроком
            if block.collide_player(self.player):
                self.update_screen()
                time.sleep(2)
                self.terminate()

    def get_input(self):
        """Обработка событий клавиатуры."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.terminate()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.terminate()
                elif event.key == pg.K_LEFT:
                    self.player.left = True
                elif event.key == pg.K_RIGHT:
                    self.player.right = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.left = False
                elif event.key == pg.K_RIGHT:
                    self.player.right = False

    @staticmethod
    def terminate():
        """Осуществляет выход из игры."""
        pg.quit()
        sys.exit()

    def update_screen(self):
        """Обновление всех игровых объектов на экране."""
        self.screen.fill(self.conf.bg_color)
        for block in self.blocks:
            block.draw(self.screen)
        self.player.draw(self.screen)
        self.score.draw(self.screen)
        self.clock.tick(self.conf.FPS)
        pg.display.flip()
