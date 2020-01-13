# LEVEL 2.py
#   by Lut99
#
# Dit is het tweede level van de puzzel. Hier zal de robots objecten
#   tegenkomen, en moet hij ze ontwijken.
#
# NOTE: Verander niks aan dit bestand!

from GameEntities.Grass import Grass
from GameObjects.Flag import Flag
from GameObjects.Rock import Rock


def load(self, object_list, entity_list, grid_size, square_size):
    """
        Load all required objects and sprites. Also loads the puzzel file with
        the program the robot executes
    """

    # Load grass on every grid
    print(f"  Achtergrond laden...")
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            entity_list.append(
                Grass((x * square_size[0], y * square_size[1], square_size[0], square_size[1]))
            )
    
    print("  Stenen plaatsen...")
    # First column
    for pos in [(2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]:
        object_list.append(Rock(pos[0], pos[1], square_size[0], square_size[1]))
    # Second column
    for pos in [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)]:
        object_list.append(Rock(pos[0], pos[1], square_size[0], square_size[1]))
    # Third column
    for pos in [(6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]:
        object_list.append(Rock(pos[0], pos[1], square_size[0], square_size[1]))

    print("  Vlag plaatsen...")
    object_list.append(Flag((8 * square_size[0], 6 * square_size[1], square_size[0], square_size[1])))

    print("  Robot plaatsen...")
    return (1, 1, "oost")
