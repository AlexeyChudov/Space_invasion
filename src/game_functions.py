import pygame
import sys
from time import sleep
from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Создает и выпускает пулю, если максимум еще не достигнут"""
    if len(bullets) < ai_settings.bullets_allowed:
        # Создаем новую пулю и помещаем её в bullets
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)


def check_keydown_events(event, ai_settings, screen, stats, sb, aliens, ship, bullets):
    if event.key == pygame.K_q:
        stats.save_absolute_record()
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        # Переместить корабль вправо
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Переместить корабль влево
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb,
                    ship, aliens, bullets)
        

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
 bullets):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, aliens, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,sb, play_button,
             ship, aliens, bullets, mouse_x, mouse_y)
        

def check_play_button(ai_settings, screen, stats, sb, play_button,
 ship, aliens, bullets, mouse_x, mouse_y):
    """ Запускает новую игру при нажатии кнопки Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb,
                    ship, aliens, bullets)



def start_game(ai_settings, screen, stats, sb,
    ship, aliens, bullets):
    """ Запуск новой игры"""
    # Сброс игровой статистики и настроек
    ai_settings.init_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    pygame.mouse.set_visible(False)

    # Обнуляем счет и уровень в начале новой игры 
    sb.prep_score()
    sb.prep_level()
    sb.prep_high_score()
    sb.prep_ships()

    # Убираем флот и пули
    aliens.empty()
    bullets.empty()

    # Создание нового флота и центрирование корабля
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()



def update_screen(ai_settings, screen, stats, sb, ship, aliens,
                    bullets, play_button):
    screen.blit(ai_settings.background, (0, 0))
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blit_me()
    aliens.draw(screen)
    sb.prep_ships
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, aliens, ship, bullets):
    """Обновляет положение пули и стирает старые пули с экрана"""
    bullets.update()
    # Удаление вышедших за край экрана пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, aliens,
     ship, bullets)


def check_bullet_alien_collision(ai_settings, screen, stats, sb, aliens,
 ship, bullets):
    """Проверка столкновений пуль и пришельцев"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    update_score(ai_settings, stats, sb, collisions)
    if len(aliens) == 0:
        # Уничтожение существующих пуль, создание нового флота и ускорение игры
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens, ship)


def update_score(ai_settings, stats, sb, collisions):
    """ Обновляет счет игры"""
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)


def check_high_score(stats, sb):
    """Обновляет рекорд игры"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
            
def get_aliens_number(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    """ Определяет сколько рядов пришельцев поместится на экране"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, ship, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (ship.rect.height + 5) + alien.rect.height * 2 * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """Создание флота пришельцев"""
    # Создание первого ряда пришельцев
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_aliens_number(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)
    # Создание первого ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Создание пришельца и размещение его на экране
            create_alien(ai_settings, screen, ship, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Проверяет достигли ли пришельцы края экрана  и меняет направление"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Опускает пришельцев и меняет направление их движения"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, aliens, bullets, ship):
    """снижает число оставшихся кораблей, убирает пули, обновляет флот"""
    if stats.ships_left > 0:
        # Снижение количества оставшихся кораблей
        stats.ships_left -= 1
        sb.prep_ships()


        # Очистка групп пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # Пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, aliens, bullets, ship):
    """ Проверяет не дошли ли пришельцы до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, aliens, bullets, ship)
            break


def update_aliens(ai_settings, screen, stats, sb, aliens, bullets, ship):
    """Проверяет достиг ли пришелец края экрана,
     затем обновляет позиции всех пришельцев во флоте"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Проверка столкновений пришельцев с кораблем
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, aliens, bullets, ship)
    # Проверка достижения пришельцами земли
    check_aliens_bottom(ai_settings, screen, stats, sb, aliens,
                        bullets, ship)
