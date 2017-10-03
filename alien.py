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
