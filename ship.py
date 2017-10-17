import pygame


class Ship:

    def __init__(self, screen, game_settings):
        """"Initialise the ship and set its starting position."""
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the centre/ bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery - this would be centre
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's centre
        self.x_axis = float(self.rect.centerx)
        self.y_axis = float(self.rect.centery)

        # Movement flag
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def update(self):
        """"Update the ship's position based on the movement flag."""
        if self.is_moving_right and self.rect.right < self.screen_rect.right:
            self.x_axis += self.game_settings.ship_speed_factor
        elif self.is_moving_left and self.rect.left > 0:
            self.x_axis -= self.game_settings.ship_speed_factor
        elif self.is_moving_up and self.rect.top > 0:
            self.y_axis -= self.game_settings.ship_speed_factor
        elif self.is_moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_axis += self.game_settings.ship_speed_factor

        self.rect.centerx = self.x_axis
        self.rect.centery = self.y_axis

    def blitme(self):
        """"Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """"Centres the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
