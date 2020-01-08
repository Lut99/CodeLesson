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


def main(screen_width, screen_height):
    print("### PUZZEL ###\n")

    print("Initializeren van PyGame...", end="")
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Puzzel")

    print(" Check")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("\nBye.\n")
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill((pygame.white))

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", "--width", help="De breedte (in pixels) van het scherm", type=int, default=800)
    parser.add_argument("-H", "--height", help="De hoogte (in pixels) van het scherm", type=int, default=600)

    args = parser.parse_args()

    # Run main
    main(args.width, args.height)
