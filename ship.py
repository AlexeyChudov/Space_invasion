import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс корабля"""
    def __init__(self, ai_settings, screen):
        """ Инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.ai_settings = ai_settings
        # Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Обновляет позицию корабля с учетом флага """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """ Появление нового корабля в центре внизу экрана"""
        self.center = self.screen_rect.centerx

    def blit_me(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
