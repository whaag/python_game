class GameStats():
    """"Track statistics for the game."""

    def __init__(self, game_settings):
        """"Initialize statistics."""
        self.game_settings = game_settings
        self.ships_left = 0
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.pilot_alive = True

    def reset_stats(self):
        """"Initialize statistics that can chnage during the game."""
        self.ships_left = self.game_settings.ship_limit
