# MAIN.py
#   by Lut99
#
# Dit bestand bevat de ingang van het programma en is dus bedoeld om uit te
#   voeren.
#
# NOTE: Verander niks aan dit bestand!
#

import sys
import pygame
import argparse
import os

from GameBase.GameTime import GameTime
from GameBase.GameLevel import Level

GRID_SIZE = 75


def main(level_name, screen_width, screen_height, framerate, updaterate):
    print("\nInitializeren van PyGame...", end="")
    pygame.init()
    pygame.font.init()
    print(" Gedaan")

    print(f"\nLevel {level_name} laden...")
    # Check if the path exists
    if not os.path.exists(f"GameLevels/{level_name}.py"):
        print(f"\nERROR: Level \"{level_name}\" is onbekend\n")
        pygame.quit()
        sys.exit()

    # If it does, load it
    level = Level(level_name, grid_size=GRID_SIZE, grid_dim=(screen_width, screen_height), show_grid=True)
    print("Level laden voltooid")

    print("\nInitializeren van scherm...", end="")
    screen = pygame.display.set_mode((screen_width * GRID_SIZE, screen_height * GRID_SIZE))
    pygame.display.set_caption("Puzzel")
    print(" Gedaan")

    print("Initializeren van framerate & update counters...", end="")
    gtime = GameTime(framerate, updaterate)
    print(" Gedaan")

    print(f"Level \"{level_name}\" laden...")

    # Main game loop
    print("\nGame loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("\nBye.\n")
                pygame.quit()
                sys.exit()

        if gtime.check_framerate():
            # Clear the screen
            screen.fill((255, 255, 255))

            # Draw the level
            level.draw(screen)

        if gtime.check_update():
            # Update the level
            level.update(gtime)

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("level_name")
    parser.add_argument("-W", "--width", help="De breedte (in vakjes) van het scherm", type=int, default=12)
    parser.add_argument("-H", "--height", help="De hoogte (in vakjes) van het scherm", type=int, default=8)
    parser.add_argument("-f", "--framerate", help="The target number of frames per second", type=int, default=30)
    parser.add_argument("-u", "--updaterate", help="The target number of updates per second", type=int, default=50)

    args = parser.parse_args()

    # Run main
    main(args.level_name, args.width, args.height, args.framerate, args.updaterate)
