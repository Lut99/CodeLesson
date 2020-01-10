# LEVEL 1.py
#   by Lut99
#
# Dit is het eerste level van de puzzel. Het doel is om te leren hoe de puzzel
#   werkt, en hoe je de bal kan aansturen.

from GameEntities.Grass import Grass
from GameObjects.Flag import Flag


def load(self, object_list, entity_list, grid_size, grid_dim):
    """
        Load all required objects and sprites. Also loads the puzzel file with
        the program the robot executes
    """

    # Load grass on every grid
    print(f"  Creating background...")
    for y in range(0, grid_dim[1] * grid_size, grid_size):
        for x in range(0, grid_dim[0] * grid_size, grid_size):
            entity_list.append(
                Grass((x, y, grid_size, grid_size))
            )

    print("  Placing flag...")
    object_list.append(Flag((8 * grid_size, 6 * grid_size, grid_size, grid_size)))

    print("  Placing robot...")
    return (0, 0, "oost")
