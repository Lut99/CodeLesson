# LEVEL 1.py
#   by Lut99
#
# Dit is het eerste level van de puzzel. Het doel is om te leren hoe de puzzel
#   werkt, en hoe je de bal kan aansturen.

from GameObjects.Robot import Robot


def load(self, object_list, entity_list):
    """
        Load all required objects and sprites. Also loads the puzzel file with
        the program the robot executes
    """

    # Initialize the robot, load the program and add it to the list
    object_list.append(
        Robot(__import__("puzzel.py", fromlist=['']).level1)
    )
