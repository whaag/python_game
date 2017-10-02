import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make an alien
    alien = Alien(game_settings, screen)

    # make a ship
    ship = Ship(screen, game_settings)
    bullets = Group()

    while True:
        gf.check_events(ship, game_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets, alien)


run_game()
