# GAME LEVEL.py
#   by Lut99
#
# Deze base class zorgt ervoor dat we makkelijk een level kunnen aanwijzen,
#   inladen en uitvoeren.

import pygame

from GameObjects.Robot import Robot


class Level():
    def __init__(self, level_name, grid_size=75, grid_dim=(12, 8), show_grid=False):
        self.show_grid = show_grid
        self.grid_size = grid_size
        self.grid_dim = grid_dim
        self.made_it = False
        self.made_it_colour = (255, 255, 0)
        self.colour_direction = -1

        # Init the win font
        self.font = pygame.font.SysFont("Ariel", 75, bold=True)

        # Load the level
        level = __import__(f"GameLevels.{level_name}", fromlist=[''])

        # Let the class load what they want
        self.objects = []
        self.entities = []
        robot_vec = level.load(self, self.objects, self.entities, self.grid_size, self.grid_dim)

        # Finally, load the robot ourselves
        self.objects.append(Robot(__import__("puzzel", fromlist=['']).level1, self, (robot_vec[0] * self.grid_size, robot_vec[1] * self.grid_size), robot_vec[2]))

    def update(self, gametime):
        """
            Updates all objects loaded by the current level if the player
            hasn't won yet. Otherwise, cycle the win colour.
        """

        if not self.made_it:
            for obj in self.objects:
                obj.update(gametime)
        else:
            r, g, b = self.made_it_colour
            g += self.colour_direction * ((255 / 2) / gametime.updaterate)
            if g <= 0:
                g = 0
                self.colour_direction = 1
            elif g >= 255:
                g = 255
                self.colour_direction = -1
            self.made_it_colour = (r, g, b)

    def draw(self, screen):
        """ Draws all objects and entities loaded by the current level """
        for ent in self.entities:
            ent.draw(screen)
        for obj in self.objects:
            obj.draw(screen)

        # If given, also print the grid
        if self.show_grid:
            for i in range(0, max(self.grid_dim)):
                if i > 0 and i < self.grid_dim[0]:
                    pygame.draw.line(screen, (0, 0, 0), (i * self.grid_size, 0), (i * self.grid_size, self.grid_dim[1] * self.grid_size))
                if i > 0 and i < self.grid_dim[1]:
                    pygame.draw.line(screen, (0, 0, 0), (0, i * self.grid_size), (self.grid_dim[0] * self.grid_size, i * self.grid_size))
        
        # Overlay the win box
        if self.made_it:
            w, h = self.font.size("JE HEBT GEWONNEN!!")
            upleft = (screen.get_size()[0] / 2 - w / 2 - 20, screen.get_size()[1] / 2 - h / 2 - 20)
            pygame.draw.rect(screen, self.made_it_colour, (upleft[0], upleft[1], w + 40, h + 40))
            screen.blit(self.font.render("JE HEBT GEWONNEN!!", False, (0, 0, 0)), (upleft[0] + 20, upleft[1] + 20))

    def move(self, obj, direction):
        """
            Moves given object horizontally or vertically. This
            movement is in grid squares and is indicate by a compass
            direction (noord, oost, zuid or west).
        """

        new_x = obj.x
        new_y = obj.y

        clip = False
        if direction == "noord":
            new_y -= self.grid_size
            if new_y < 0:
                new_y = 0
                clip = True
        elif direction == "oost":
            new_x += self.grid_size
            if new_x > (self.grid_dim[0] - 1) * self.grid_size:
                new_x = (self.grid_dim[0] - 1) * self.grid_size
                clip = True
        elif direction == "zuid":
            new_y += self.grid_size
            if new_y > (self.grid_dim[1] - 1) * self.grid_size:
                new_y = (self.grid_dim[1] - 1) * self.grid_size
                clip = True
        elif direction == "west":
            new_x -= self.grid_size
            if new_x < 0:
                new_x = 0
                clip = True
        else:
            raise ValueError("direction can only be 'noord', 'oost', 'zuid' or 'west'")

        # Check if anything is already here that is not-crossable
        for obj_2 in self.objects:
            if obj_2.x == new_x and obj_2.y == new_y and not obj_2.crossable:
                return True
        for ent in self.entities:
            if ent.x == new_x and ent.y == new_y and not ent.crossable:
                return True
        
        # If there isn't update the value
        obj.x = new_x
        obj.y = new_y

        return clip

    def get(self, x, y):
        """
            Returns the object that is at x, y in the grid. If the grid is
            out of bounds, the string "OutOfBounds" is returned. If no
            object is present (regardless if an entity is), return "Air".
        """

        if x < 0 or x > self.grid_dim[0] or y < 0 or y > self.grid_dim[0]:
            return "OutOfBounds"

        for obj in self.objects:
            if obj.x == x * self.grid_size and obj.y == y * self.grid_size:
                return obj

        return "Air"

    def win(self):
        """ If called, adds the win box to the level. """

        self.made_it = True
        print("\nGEFELICITEERD! Je hebt het level gehaald!")
        print("Zet het programma uit, en open het volgende level door de naam van dat level in te voeren.")