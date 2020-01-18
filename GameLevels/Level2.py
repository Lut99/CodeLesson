# LEVEL 2.py
#   by Lut99
#
# Created:
#   1/18/2020, 1:02:59 PM
# Last edited:
#   1/18/2020, 2:26:47 PM
# Auto updated?
#   Yes
#
# Description:
#   In dit bestand is het tweede level beschreven. Het idee is dat de robot
#   moet kijken waar de een struik zich bevind en er naartoe lopen, omdat hij
#   begint op een willekeurige X op tweede rij en de vlag helemaal rechts op
#   de zevende rij staat.
#
# NOTE: Verander niks aan dit bestand!
#

import random

from GameEntities.Grass import Grass
from GameObjects.Flag import Flag
from GameObjects.Bush import Bush


def load(self, object_list, entity_list, grid_size, square_size):
    """
        Load all required objects and sprites for this level.
    """

    # Load grass on every grid
    print("  Creating background...")
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            entity_list.append(
                Grass((x * square_size[0], y * square_size[1], square_size[0], square_size[1]))
            )

    # Place a few bushes as decoration
    print("  Placing bushes...")
    for x, y in [(8, 1), (2, 4), (5, 7), (0, 3), (6, 0), (6, 4)]:
        object_list.append(
            Bush((x * square_size[0], y * square_size[1], square_size[0], square_size[1]))
        )

    # Place the flag
    print("  Placing flag...")
    object_list.append(Flag((random.randint(2, 7) * square_size[0], square_size[1], square_size[0], square_size[1])))

    # Place the robot
    return (1, 1, "oost")
