import pygame


class Character:
    """Class to manage the characters"""

    def __init__(self, ai_game):
        """Initilaise the elephant an its position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/elephant.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
