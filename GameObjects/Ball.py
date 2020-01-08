# BAL.py
#   by Lut99
#
# Dit bestand bevat de class voor de Bal. Het is een derived class van
#   GameObject, en bedoeld om te worden bewogen in de puzzel.

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite


# Represents a Ball
class Ball(GameObject):
    def __init__(self):
        super().__init__(sprite=Sprite("GameObjects/sprites/ball.jpg", size=(100, 100)))

        # Set position
        self.x = 350
        self.y = 250
        self.w = 100
        self.h = 100
