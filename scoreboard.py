import pygame.font


class Scoreboard:
    """"A class to report the score."""
    
    def __init__(self, game_settings, screen, stats):
        """"Initialise the score attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        
        # Font setting for scoring info.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """"Turn the score into a rendered iage."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """"Draws the score."""
        self.screen.blit(self.score_image, self.score_rect)
