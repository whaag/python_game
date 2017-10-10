import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_events(ship, game_settings, screen, bullets):
    """"Respond to keypress and mouse events."""
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


def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets and create new armada.
        bullets.empty()
        game_settings.alien_speed_factor += 0.5
        create_armada(game_settings, screen, aliens, ship)


def update_bullets(bullets, aliens, ship, game_settings, screen):
    """"Update bullets position's and get rid of old ones."""
    bullets.update()

    # Get rid of out of screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets)


def get_number_aliens_x(game_settings, alien_width):
    """"Calculate the number of aliens that fit in a row."""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """"Create an alien and place it in the row."""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_armada(game_settings, screen, aliens, ship):
    """"Create an alien armada."""
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def get_number_rows(game_settings, ship_height, alien_heigt):
    """"Determine the number of rows of aliens that fit on the secreen."""
    available_spcae_y = (game_settings.screen_height - (3 * alien_heigt) - ship_height)
    number_rows = int(available_spcae_y / (2 * alien_heigt))
    return number_rows


def update_aliens(aliens, game_settings):
    """"Update the positions of the aliens in the armada."""
    check_armada_edges(game_settings, aliens)
    aliens.update()


def change_armada_direction(game_settings, aliens):
    """"Drop the entire armada and change its direction."""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.armada_drop_speed
    game_settings.armada_direction *= -1


def check_armada_edges(game_settings, aliens):
    """"Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_armada_direction(game_settings, aliens)
            break
