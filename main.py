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
from GameLevels.LevelSelector import LevelSelector

GRID_SIZE = 75


def main(framerate, updaterate):
    print("\nInitializeren van PyGame...", end="")
    pygame.init()
    pygame.font.init()
    print(" Gedaan")

    print("\nInitializeren van scherm...", end="")
    screen = pygame.display.set_mode((12 * GRID_SIZE, 8 * GRID_SIZE))
    pygame.display.set_caption("Puzzel")
    print(" Gedaan")

    print("\nInitializeren van framerate & update counters...", end="")
    gtime = GameTime(framerate, updaterate)
    print(" Gedaan")

    # print("\nLaden van level selector...")
    # selector = LevelSelector()
    # print("Level selector geladen.")

    # print("\nWachten tot een level is gekozen...")
    # level_name = selector.select()
    # if level_name == "None":
    #     # No level has been chosen
    #     print("\nGeen level gekozen.\n\nBye.\n")
    #     pygame.quit()
    #     sys.exit()
    # print(f"Gekozen level: {level_name}")

    # print(f"\nLevel \"{level_name}\" laden...")
    # # Check if the path exists
    # if not os.path.exists(f"GameLevels/{level_name}.py"):
    #     print(f"\nERROR: Level \"{level_name}\" is onbekend\n")
    #     pygame.quit()
    #     sys.exit()

    # # If it does, load it
    # level = Level(level_name, grid_size=GRID_SIZE, grid_dim=(12 * GRID_SIZE, 8 * GRID_SIZE), show_grid=False)
    # print("Level laden voltooid")

    print("\nLaden van level selector...")
    level = LevelSelector()
    print("Level selector geladen.")

    # Main game loop
    print("\nGame loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if type(level) == LevelSelector:
                    if event.key == pygame.K_UP:
                        if level.selected > 1:
                            level.selected -= 2
                    elif event.key == pygame.K_RIGHT:
                        if level.selected < len(level.levels) - 1:
                            level.selected += 1
                    elif event.key == pygame.K_DOWN:
                        if level.selected < len(level.levels) - 2:
                            level.selected += 2
                    elif event.key == pygame.K_LEFT:
                        if level.selected > 0:
                            level.selected -= 1
                    elif event.key == pygame.K_RETURN:
                        # Enter has been pressed: switch to the selected level
                        level_name = level.levels[level.selected].name
                        print(f"\nGekozen level: \"{level_name}\" laden...")
                        level = Level(level_name, grid_size=GRID_SIZE, grid_dim=(12, 8), show_grid=False)
                        print(f"\nLevel: \"{level_name}\" geladen")
            elif event.type == pygame.QUIT:
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
    parser.add_argument("-f", "--framerate", help="The target number of frames per second", type=int, default=30)
    parser.add_argument("-u", "--updaterate", help="The target number of updates per second", type=int, default=50)

    args = parser.parse_args()

    # Run main
    main(args.framerate, args.updaterate)
