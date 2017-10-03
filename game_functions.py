import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_events(ship, game_settings, screen, bullets):
    """"Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, game_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship, game_settings, screen, bullets):
    """"Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = True
    elif event.key == pygame.K_UP:
        ship.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.is_moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """"Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = False
    elif event.key == pygame.K_UP:
        ship.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.is_moving_down = False


def update_screen(game_settings, screen, ship, bullets, aliens):
    """"Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop.
    screen.fill(game_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def fire_bullet(game_settings, screen, ship, bullets):
    """"Fire a bullet if available."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < game_settings.max_bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """"Update bullets position's and get rid of old ones."""
    bullets.update()

    # Get rid of out of screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_armada(game_settings, screen, aliens):
    """"Create an alien armada."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # create the first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
