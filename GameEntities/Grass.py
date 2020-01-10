# GRASS.py
#   by Lut99
#
# Deze class representeerd een gras entitiy in de puzzel.
#
# NOTE: Verander niks aan dit bestand!

from GameBase.Sprite import Sprite
from GameBase.GameEntity import GameEntity


class Grass(GameEntity):
    def __init__(self, rect):
        super().__init__(rect, sprite=Sprite("GameEntities/sprites/grass.png", size=(rect[2], rect[3])))

        print(f"GRASS:: Got created on {self.x}, {self.y}")