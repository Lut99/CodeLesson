# LEVEL SELECTOR.py
#   by Lut99
#
# Grafische interface die de gebruiker een level laat uitkizen.
#
# NOTE: Verander niks aan dit bestand!

import os
import pygame


class LevelChoice():
    def __init__(self, name, font):
        self.name = name
        self.path = "GameLevels/" + self.name + ".py"
        self.import_path = "GameLevels." + self.name

        # Already calculate the width and height of the text required
        self.font = font
        self.tw, self.th = self.font.size(self.name)
        self.w, self.h = self.tw + 20, self.th + 20

    def __lt__(self, other):
        return self.name < other.name


class LevelSelector():
    def __init__(self):
        # Declare the font (title, level names and help text)
        self.font_title = pygame.font.SysFont("Ariel", 50, bold=True)
        self.font_level = pygame.font.SysFont("Ariel", 24)
        self.font_help = pygame.font.SysFont("Ariel", 30)

        # Also declare static text pieces
        self.title = self.font_title.render("Kies een level:", False, (0, 0, 0))
        self.title_w, self.title_h = self.font_title.size("Kies een level:")
        self.help = self.font_help.render("Kies een level met de pijltjestoetsen, en druk op Enter om te beginnen.", False, (0, 0, 0))
        self.help_w, self.help_h = self.font_help.size("Kies een level met de pijltjestoetsen, en druk op Enter om te beginnen.")

        # Escape if the target folder doesn't exist
        if not os.path.isdir("GameLevels/"):
            raise FileNotFoundError("No folder \"./GameLevels/\" found")

        # Search for files with desired name pattern
        files = [f for f in os.listdir("GameLevels/") if os.path.isfile(f"GameLevels/{f}")]
        self.levels = []
        for f in files:
            if f != "LevelSelector.py" and f[-3:] == ".py":
                # We found a level file
                self.levels.append(LevelChoice(f[:-3], self.font_level))

        # Sort that list alphabetically
        self.levels.sort()

        # Initialize self.selected to first value (by default)
        self.selected = 0

    def update(self, events):
        """
            Updates the level selector. Note that thins actually does nothing,
            but serves to intergrate easily with levels.
        """

        pass

    def draw(self, screen):
        """
            Draws the level selector. Note that this is called as if it's a
            normal level.
        """

        # First, draw the title in the topleft
        screen.blit(self.title, (10, 10))

        # Then, draw each level (two per row, no scrolling for now)
        i = 0
        for lvl in self.levels:
            w, h = (screen.get_size()[0] - 30) / 2, 40
            x, y = 10, 10 + self.title_h + 10 + (i // 2) * (h + 10)
            if i % 2 == 1:
                # Second half instead
                x = screen.get_size()[0] / 2 + 5

            # Draw the box first on the specified location
            if self.selected == i:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h))
                screen.blit(self.font_level.render(lvl.name, False, (255, 255, 255)), (x + 10, y + 10))
            else:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h), 1)
                screen.blit(self.font_level.render(lvl.name, False, (255, 0, 0)), (x + 10, y + 10))

            i += 1

        # Finally, draw the help text in the bottom corner
        screen.blit(self.help, (10, screen.get_size()[1] - 10 - self.help_h))
