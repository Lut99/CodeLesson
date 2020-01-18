# LEVEL 1.py
#   by Lut99
#
# Dit is het eerste level van de puzzel. Het doel is om te leren hoe de puzzel
#   werkt, en hoe je de bal kan aansturen.

from GameEntities.Grass import Grass
from GameObjects.Flag import Flag


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
    object_list.append(Flag((8 * square_size[0], 6 * square_size[1], square_size[0], square_size[1])))

    print("  Placing robot...")
    return (1, 1, "oost")
