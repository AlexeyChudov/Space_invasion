import pygame.font

class Button():
    """Создает кнопку для начала игры"""
    def __init__(self, ai_saettings, screen, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect() 

        # Задает параметры кнопки
        self.width, self.height = 200, 50
        self.button_color = (200, 100, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Создание объекта rect кнопки и выравнивание его по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)


    def prep_msg(self, msg):
        """ Преобразует текст в изображение и размещает его по центру кнопки"""
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        

