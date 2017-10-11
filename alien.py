import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """"Class that represents a single alien entity."""

    def __init__(self, game_settings, screen):
        """"Initialize the alien an set its start position."""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Loda the alien image and set its rec attribute.
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near thop left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """"Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"Move ET right or left."""
        self.x += (self.game_settings.alien_speed_factor *
                   self.game_settings.armada_direction)
        self.rect.x = self.x

    def check_edges(self):
        """"Return true if the alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
