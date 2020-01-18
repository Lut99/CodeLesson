# BUSH.py
#   by Lut99
#
# Created:
#   1/18/2020, 1:07:59 PM
# Last edited:
#   1/18/2020, 2:28:59 PM
# Auto updated?
#   Yes
#
# Description:
#   Dit bestand bevat de code voor een Bush (struik). Dit object is bedoeld
#   als obstakel, maar kan ook dienen als decoratie.
#
# NOTE: Verander niks aan dit bestand!
#

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite


class Bush(GameObject):
    def __init__(self, rect):
        super().__init__("struik", rect, sprite=Sprite("GameObjects/sprites/bush.png"), crossable=False)

    def update(self, gametime):
        super().update(self, (self.x, self.y, self.w, self.h), self.rotation)
