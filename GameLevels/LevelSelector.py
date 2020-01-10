# LEVEL SELECTOR.py
#   by Lut99
#
# Grafische interface die de gebruiker een level laat uitkizen.
#
# NOTE: Verander niks aan dit bestand!

import os


class LevelChoice():
    def __init__(self, name):
        self.name = name
        self.path = "GameLevels/" + self.name


class LevelSelector():
    def __init__(self):
        # Escape if the target folder doesn't exist
        if not os.path.isdir("GameLevels/"):
            raise FileNotFoundError("No folder \"./GameLevels/\" found")

        # Search for files with desired name pattern
        files = [f for f in os.listdir("GameLevels/") if os.path.isfile(f)]
        levels_to_choose = []
        for f in files:
            if f != "LevelSelector.py" and f[:5] == "Level" and f[-3:] == ".py":
                # We found a level file
                levels_to_choose.append(f)
