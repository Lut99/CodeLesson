# ROCK.py
#   by Lut99
#
# Dit bestand beschrijf een Rock-object. Dit is bedoeld als obstakel voor de
#   robot.
#
# NOTE: Verander niks aan dit bestand!

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite


class Rock(GameObject):
    def __init__(self, rect):
        self._sprite = Sprite("GameObjects/sprites/rock.png")

        super().__init__("Steen", rect, sprite=self._sprite, crossable=False)
