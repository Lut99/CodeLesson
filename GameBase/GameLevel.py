# GAME LEVEL.py
#   by Lut99
#
# Deze base class zorgt ervoor dat we makkelijk een level kunnen aanwijzen,
#   inladen en uitvoeren.

import pygame


class Level():
    def __init__(self, level_name, grid_size=50, show_grid=False):
        self.grid_size = grid_size
        self.show_grid = show_grid

        # Load the level
        level = __import__(f"GameLevels.{level_name}", fromlist=[''])

        # Let the class load what they want
        self.objects = []
        self.entities = []
        level.load(self, self.objects, self.entities)

    def update(self, gametime):
        """ Updates all objects loaded by the current level """
        for obj in self.objects:
            obj.update(gametime)

    def draw(self, screen):
        """ Draws all objects and entities loaded by the current level """
        for ent in self.entities:
            ent.draw(screen)
        for obj in self.objects:
            obj.draw(screen)

        # If given, also print the grid
        if self.show_grid:
            for i in range(0, 1500, self.grid_size):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 1499))
                pygame.draw.line(screen, (0, 0, 0), (0, i), (1499, i))

    def move(self, obj, x=0, y=0):
        """
            Moves given object horizontally, vertically or both. This
            movement is in grid squares and therefore has to be
            integral values. Negative is left or up, positive is right or down.
        """

        # Check if integral
        if int(x) != x or int(y) != y:
            raise ValueError("x and y have to be whole numbers")

        obj.x += x * self.grid_size
        obj.y += y * self.grid_size
