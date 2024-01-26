import pygame
from pygame.sprite import Sprite

class Alien:
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image,
                                            (50, int(self.image.get_height() * 50 / self.image.get_width())))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
