import pygame
import os


class Settings():
    def __init__(self):
        """ Инициализация статических настроек игры"""
        # Параметры экрана
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.background = pygame.image.load(r'images\bg.bmp')
        self.background = pygame.transform.smoothscale(self.background, (self.screen_width, self.screen_height))

        # Параметры корабля
        self.ship_limit = 3

        # Параметры пришeльцев
        self.fleet_drop_speed = 30

        # Параметры пуль
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Ускорение игры
        self.speedup_scale = 1.5

        # Увеличение стоимости пришельцев
        self.score_scale = 1.5

        self.init_dynamic_settings()


    def init_dynamic_settings(self):
        """Инициализирует динамические настройки игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 2

        # 1 - движение вправо, -1 - движение влево
        self.fleet_direction = 1

        # Количество очков за каждого пришельца
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает скорость игры  и стоимость пришельцев"""
        self.ship_speed_factor *=  self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
