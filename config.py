import math


class Config:
    def __init__(self):
        # General
        # Ширина окна
        self.window_width = 480
        # Высота окна
        self.window_height = 640
        # Цвет фона игры
        self.bg_color = (0, 0, 0)
        # Количество проходов основного цила игры в секуду
        self.FPS = 150

        # Player
        # Радиус окружности, по которой двигаются объекты игрока
        self.circle_radius = 80
        # Радиус объекта игрока
        self.player_radius = 15
        # Ширина и высота объекта игрока, при представлении квадратом
        self.player_width = self.player_height = self.player_radius * 2 * math.sin(45 * math.pi / 180)
        # Координаты центра окружности, по которой двигаются объекты игрока
        self.circle_centerx = self.window_width // 2
        self.circle_centery = self.window_height - self.circle_radius - self.player_radius
        # Цвета объектов игрока
        self.player_color_1 = (217, 105, 0)
        self.player_color_2 = (7, 90, 184)

        # Block
        self.block_color = (255, 255, 255)

        # Score
        self.score_font_size = 24
        self.score_color = (255, 255, 255)
