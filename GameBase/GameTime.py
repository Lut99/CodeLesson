# GAME TIMER.py
#   by Lut99
#
# Class die de tijd bijhoudt en bepaald wanneer een object moet worden
#   getekend of geupdate. Daarnaast kan het ook worden gebruikt om te kijken
#   of er een seconde voorbij is gegaan.

import time


class GameTime():
    def __init__(self, framerate, updaterate, reset_timeout=1):
        self.framerate = framerate
        self.frametime = 1 / framerate
        self.updaterate = updaterate
        self.updatetime = 1 / updaterate

        self._last_framerate_check = time.time()
        self._last_update_check = time.time()
        self._start_time = time.time()

        self._reset_timeout = 1

    def check_framerate(self):
        """
            check_framerate() returns true if it's time for another frame to be
            drawn. Returns True if it is, or False if it isn't. Note that, if
            the frame check if called extremely late after the previous frame,
            the time is reset instead of added with a constant amount.
        """

        if time.time() - self._last_framerate_check >= self.frametime:
            # A framerate occurs! Check if it was too long ago
            if time.time() - self._last_framerate_check >= self._reset_timeout:
                # Reset it
                self._last_framerate_check = time.time()
            else:
                self._last_framerate_check += self.frametime
            return True
        return False

    def check_update(self):
        """
            check_update() returns true if it's time for another update cycle.
            Returns True if it is, or False if it isn't. Note that, if the
            update check is called extremely late after the previous frame,
            the time is reset instead of added with a constant amount.
        """

        if time.time() - self._last_update_check >= self.frametime:
            # A framerate occurs! Check if it was too long ago
            if time.time() - self._last_update_check >= self._reset_timeout:
                # Reset it
                self._last_update_check = time.time()
            else:
                self._last_update_check += self.frametime
            return True
        return False

    def check_second(self):
        """
            check_second() returns true if a second has passed. Returns True if
            it is, or False if it isn't. Note that this isn't relative to the
            previous call, but rather to the start time of the class.
        """

        time_passed = time.time() - self._start_time
        second_offset = time_passed - int(time_passed)

        # Return whether a whole second has passed since the start of the class
        return second_offset < 0.01

    def get_seconds(self):
        """
            get_seconds() returns the (whole) number of seconds that the class
            has been alive.
        """

        return int(time.time() - self._start_time)
