# BAL.py
#   by Lut99
#
# Dit bestand bevat de class voor de Bal. Het is een derived class van
#   GameObject, en bedoeld om te worden bewogen in de puzzel.

from GameBase.GameObject import GameObject


# Represents a Ball
class Ball(GameObject):
    def __init__(self):
        super().__init__()

        # Set position
        self.x = 350
        self.y = 250
        self.w = 100
        self.h = 100
