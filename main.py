import sys
sys.path.insert(1, 'pygame')
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import Gamestats
from scoreboard import Scoreboard
from button import Button


def run_game():
    """Инициализация игры и создание объекта экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    background = ai_settings.background
    screen.blit(background, (0, 0))
    pygame.display.set_caption('Alien invasion')
    # Создаем корабль, пули и пришельцев
    ship = Ship(ai_settings, screen)
    aliens = Group() 
    gf.create_fleet(ai_settings, screen, aliens, ship)
    bullets = Group()
    # Создание экземпляров Gamestats и Scoreboard
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")
    while True:
        # Отслеживание событий игры
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,   bullets)
        if stats.game_active: 
            ship.update()
            sb.prep_ships
            gf.update_bullets(ai_settings, screen, stats, sb, aliens, ship, bullets) 
            gf.update_aliens(ai_settings, screen, stats, sb, aliens, bullets, ship)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                            bullets, play_button)


run_game()





