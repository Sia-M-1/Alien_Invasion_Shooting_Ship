import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

# Запуск основного цикла игры.
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)
    # Создание корабля.
    ship = Ship(ai_settings,screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    # Создание пришельцев
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game( )
