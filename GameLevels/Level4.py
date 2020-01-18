# LEVEL 4.py
#   by Lut99
#
# Created:
#   1/18/2020, 2:16:25 PM
# Last edited:
#   1/18/2020, 2:26:17 PM
# Auto updated?
#   Yes
#
# Description:
#   In dit bestand staat de beschrijving van Level3. In dit level moet de
#   speler de robot naar de vlag toe loodsen die een willekeurige positie
#   heeft. De speler krijgt een leeg veld met de robot altijd op (1, 1), en
#   kan de positie van de vlag opvragen met robot.kijk_vlag()
#
# NOTE: Verander niks aan dit bestand!
#

from GameEntities.Grass import Grass
from GameObjects.Flag import Flag

import random


def load(self, object_list, entity_list, grid_size, square_size):
    """
        Load all required objects and sprites. Also loads the puzzel file with
        the program the robot executes
    """

    # Load grass on every grid
    print(f"  Creating background...")
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            entity_list.append(
                Grass((x * square_size[0], y * square_size[1], square_size[0], square_size[1]))
            )

    print("  Placing flag...")
    flag_x, flag_y = random.randint(1, 9), random.randint(1, 7)
    if flag_x == 1 and flag_y == 1:
        flag_x, flag_y = random.randint(2, 9), random.randint(2, 7)

    object_list.append(Flag((flag_x * square_size[0], flag_y * square_size[1], square_size[0], square_size[1])))

    print("  Placing robot...")
    return (1, 1, "oost")
