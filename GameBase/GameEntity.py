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


class GameEntity():
    def __init__(self, rect, sprite=None, crossable=True):
        self._sprite = sprite

        self.x, self.y, self.w, self.h = rect

        self.visible = False
        self.crossable = crossable

    def draw(self, screen):
        # Update the sprite if there is one
        if self._sprite is not None:
            # Draw the sprite class
            self._sprite.draw(screen)
        else:
            # Simply draw a black rectangle
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h))
