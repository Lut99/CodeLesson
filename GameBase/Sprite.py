# SPRITE.py
#   by Lut99
#
# Class die informatie opslaat over een sprite voor PyGame. Ondersteund
#   automatisch laden van foto's en het tekenen ervan.

import pygame


class Sprite():
    def __init__(self, path_to_picture, size=(0, 0)):
        self._img = pygame.image.load(path_to_picture)
        self._scaled_img = pygame.transform.scale(self._img, size)

        self.x = 0
        self.y = 0
        self.w, self.h = size

    def update(self, rect):
        """
            Updates the sprite, as in: gives it a new position and possibly
            rescales the image if the size has changed.
        """

        # Rescale the image if necessary
        if self.w != rect[2] or self.h != rect[3]:
            self._scaled_img = pygame.transform.scale(self._img, (rect[2], rect[3]))

        # Store the new values
        self.x, self.y, self.w, self.h = rect

    def draw(self, screen):
        """ Draws the sprite on stored location. """
        screen.blit(self._scaled_img, (self.x, self.y))
