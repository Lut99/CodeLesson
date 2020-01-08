# BAL.py
#   by Lut99
#
# Dit bestand bevat de class voor de Bal. Het is een derived class van
#   GameObject, en bedoeld om te worden bewogen in de puzzel. Daarnaast
#   is er ook de Programma subclass van de Robot, die gebruikt wordt om hem
#   te programmeren.

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite


DIRECTIONS = [
    "noord", "oost", "zuid", "west",
    "boven", "rechts", "onder", "links"
]


class Program:
    """
        The program class is an interface to the robot that is used in the
        puzzel file. Upon calling an instruction, the instruction passes this
        to the robot object and waits until the waiting time has passed before
        continuing.
    """

    NOORD = "noord"
    OOST = "oost"
    ZUID = "zuid"
    WEST = "west"
    BOVEN = "boven"
    RECHTS = "rechts"
    ONDER = "onder"
    LINKS = "links"

    def __init__(self, gametime):
        self._instructions = []

    def stap(self, direction, amount=1):
        """
            Makes the robot walk amount steps in the direction he is pointing
            at at the moment.
        """

        pass

    def pak_vast(self):
        """
            Grabs something that is in front of the robot. If there is nothing,
            nothing is grabbed.
        """

        pass

    def laat_los(self):
        """
            Lets whatever the robot is holding go. If he is holding nothing,
            nothing is dropped.
        """

        pass

    def draai(self, direction):
        """
            Turns the robot to the specified direction. This is absolute, not
            relative to the current rotation. The user can input Noord, Oost,
            Zuid or West for absolute rotations, and Boven, Rechts, Onder,
            Links for relative rotation.
        """

        pass


    def kijk(self):
        """
            Geeft terug wat er voor de robot staat.
        """

        pass


# Represents the Robot (player)
class Robot(GameObject):
    def __init__(self, program):
        super().__init__((0, 0, 75, 75), sprite=Sprite("GameObjects/sprites/robot1.png"))

        # Run the program on the robot thread
        
    def __del__(self):
        # Stop the execution thread

    def update(self, gametime):
        super().update(gametime, (self.x, self.y, self.w, self.h))