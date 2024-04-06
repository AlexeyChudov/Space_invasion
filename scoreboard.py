import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Класс табло для вывода статистики на экран"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Параметры текста
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.text_bg_color = (0, 0, 0)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.text_bg_color)

        # Вывод счета в правом верхнем углу
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Преобразует рекорд в изображение"""
        high_score = round(self.stats.high_score, -1) 
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,  True,
        self.text_color, self.text_bg_color)

        # Вывод счета в центре сверху
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.text_bg_color)

        # Уровень выводится под текущим счетом
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10 

    def prep_ships(self):
        """ Прорисовывает число кораблей в левом верхнем углу экрана"""
        self.ships = Group()
        ships_left = self.stats.ships_left
        for ship_number in range(ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)  
            
    def show_score(self):
        """Выводит счет на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

