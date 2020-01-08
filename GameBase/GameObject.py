# GAME OBJECT.py
#   by Lut99
#
# De GameObject Class is afgeleid van de GameEntity class en is de basis voor
#   alle beweegbare objecten in de puzzel.

from GameBase.GameEntity import GameEntity


class GameObject(GameEntity):
    def __init__(self):
        super().__init__()

    def update(self, gametime):
        # Update the position
        super().update(gametime, (350, 250, 100, 100))

    def draw(self, screen):
        super().draw(screen)
