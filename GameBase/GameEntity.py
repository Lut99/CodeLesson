# GAME ENTITY.py
#   by Lut99
#
# The basis class voor alles wat tekenbaar is in de puzzel. Bevat een draw
#   functie, die de sprite tekend op de gewenste plek, en de update functie,
#   die het object update (bijvoorbeeld volgende stap in een animatie,
#   verplaatsing van een object, etc).
#
# NOTE: Verander niks aan dit bestand!

from GameBase.Sprite import Sprite


class GameEntity():
    def __init__(self, x, y, w, h, visible=False, sprite=None):
        self._sprite = sprite

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.visible = visible

    def update(self, gametime):
        pass

    def draw(self, screen, gametime):
        pass
