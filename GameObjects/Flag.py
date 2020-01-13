# FLAG.py
#   by Lut99
#
# Dit bestand host de Flag class, die, wanneer aangeraakt, de speler het level
#   laat winnen.
#
# NOTE: Verander niks aan dit bestand!

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite
from GameBase.GameTime import Timer


class Flag(GameObject):
    def __init__(self, rect):
        self._sprite1 = Sprite("GameObjects/sprites/flag1.png")
        self._sprite2 = Sprite("GameObjects/sprites/flag2.png")

        super().__init__("Flag", rect, sprite=self._sprite1)

        self._timer = Timer(0.5)

    def update(self, gametime):
        # Swap sprite if needed
        if gametime.check_timer(self._timer):
            self._timer.reset()

            if self._sprite == self._sprite1:
                self._sprite = self._sprite2
            else:
                self._sprite = self._sprite1

        super().update(gametime, (self.x, self.y, self.w, self.h), self.rotation)
