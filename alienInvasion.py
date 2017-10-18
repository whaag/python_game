import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store statistics.
    stats = GameStats(game_settings)
    scoreboard = Scoreboard(game_settings, screen, stats)

    # Creates a button
    play_button = Button(game_settings, screen, "Play")

    # make a ship, a group of bullets, and a group of aliens.
    ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()

    # Create an alien armada
    gf.create_armada(game_settings, screen, aliens, ship)

    while True:
        gf.check_events(ship, game_settings, screen, bullets, stats, play_button, aliens)

        if stats.pilot_alive:
            ship.update()
            gf.update_bullets(bullets, aliens, ship, game_settings, screen, stats, scoreboard)
            gf.update_aliens(aliens, game_settings, ship, stats, screen, bullets)

        gf.update_screen(game_settings, screen, ship, bullets, aliens, stats, play_button, scoreboard)


run_game()
