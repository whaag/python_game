class Settings:
    """"A class to store all settings for the game."""

    def __init__(self):
        """"Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 3
        self.max_bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.armada_drop_speed = 10
        # armada_direction of 1 represents right; -1 left
        self.armada_direction = 1
