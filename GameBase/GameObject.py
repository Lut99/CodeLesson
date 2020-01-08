# GAME OBJECT.py
#   by Lut99
#
# De GameObject Class is afgeleid van de GameEntity class en is de basis voor
#   alle beweegbare objecten in de puzzel.

from GameBase.GameEntity import GameEntity


class GameObject(GameEntity):
    def __init__(self, rect, sprite=None):
        super().__init__(rect, sprite=sprite)

    def update(self, gametime, rect):
        # Update the position and size with a newly given one
        self.x, self.y, self.w, self.h = rect

        # Pass to sprite
        if self._sprite is not None:
            self._sprite.update(rect)

    def draw(self, screen):
        super().draw(screen)
