# GAME ENTITY.py
#   by Lut99
#
# The basis class voor alles wat tekenbaar is in de puzzel. Bevat een draw
#   functie, die de sprite tekend op de gewenste plek, en de update functie,
#   die het object update (bijvoorbeeld volgende stap in een animatie,
#   verplaatsing van een object, etc).
#
# NOTE: Verander niks aan dit bestand!

import pygame

from GameBase.Sprite import Sprite


class GameEntity():
    def __init__(self, sprite=None):
        self._sprite = sprite

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

        self.visible = False

    def update(self, gametime, rect):
        # Set own rectangle values
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]

    def draw(self, screen):
        # Update the sprite if there is one
        if self._sprite is not None:
            # Draw the sprite class
            self._sprite.draw(screen, (self.x, self.y, self.w, self.h))
        else:
            # Simply draw a black rectangle
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h))
