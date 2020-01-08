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
import random

from GameBase.GameTime import GameTime
from GameObjects.Ball import Ball


def main(screen_width, screen_height, framerate, updaterate):
    print("### PUZZEL ###\n")

    print("Initializeren van PyGame...", end="")
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Puzzel")
    print(" Check")

    print("Initializeren van framerate & update counters...", end="")
    gtime = GameTime(framerate, updaterate)
    print(" Check")

    print(f"Level \"{'lol'}\" laden...", end="")
    ball = Ball()
    print(" Check")

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

            # Draw object
            ball.draw(screen)

        if gtime.check_update():
            ball.update(gtime)

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", "--width", help="De breedte (in pixels) van het scherm", type=int, default=800)
    parser.add_argument("-H", "--height", help="De hoogte (in pixels) van het scherm", type=int, default=600)
    parser.add_argument("-f", "--framerate", help="The target number of frames per second", type=int, default=30)
    parser.add_argument("-u", "--updaterate", help="The target number of updates per second", type=int, default=50)

    args = parser.parse_args()

    # Run main
    main(args.width, args.height, args.framerate, args.updaterate)
