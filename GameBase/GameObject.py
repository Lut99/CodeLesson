# GAME OBJECT.py
#   by Lut99
#
# De GameObject Class is afgeleid van de GameEntity class en is de basis voor
#   alle beweegbare objecten in de puzzel.

from GameBase.GameEntity import GameEntity


class GameObject(GameEntity):
    def __init__(self, rect, sprite=None, rotation="oost", crossable=True):
        super().__init__(rect, sprite=sprite, crossable=crossable)

        self.rotation = rotation

    def update(self, gametime, rect, rotation):
        # Update the position and size with a newly given one
        self.x, self.y, self.w, self.h = rect
        self.rotation = rotation

        # Pass to sprite
        if self._sprite is not None:
            self._sprite.update(rect, self.rotation)

    def draw(self, screen):
        super().draw(screen)
