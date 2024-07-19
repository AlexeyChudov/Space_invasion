import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """класс, представляющий одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализация пришельца"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Загружаем пришельца
        self.image = pygame.image.load(r'images/alien_realistic.bmp')
        self.rect = self.image.get_rect()

        # Определяем координаты пришельца(левый верхний угол)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Вещественная координата
        self.x = float(self.rect.x)

    def check_edges(self):
        """Проверяет достиг ли пришелец края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает корабль вправо или влево"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blit_me(self):
        """Выводит корабль на экран"""
        self.screen.blit(self.image, self.rect)
