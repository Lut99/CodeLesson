# GAME TIMER.py
#   by Lut99
#
# Class die de tijd bijhoudt en bepaald wanneer een object moet worden
#   getekend of geupdate. Daarnaast kun je ook timers laten runnen om te testen
#   of er een specifiek tijdstip voorbij is gegaan.
#
# NOTE: Verander niks aan dit bestand!

import time


class Timer():
    def __init__(self, target_timeout):
        self._target = time.time() + target_timeout
        self._timeout = target_timeout

    def reset(self, relative=False):
        """
            Resets the timer to time.time() + self._timeout again. If relative
            is set to True, then the timer is set to
            self._target += self._timeout. The last option is more precise, but
            can easily start to lag behind.
        """

        self._target = time.time() + self._timeout

    def new_target(self, target_timeout):
        """ Resets the timer to a new timeout time """
        self._target = time.time() + target_timeout
        self._timeout = target_timeout

    def stop(self):
        """ Disables the timer so that it never occurs """
        self._target = float("inf")

    def start(self):
        """ Same as non-relative reset """
        self.reset()


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

    def set_timer(self, seconds_to_go):
        """
            Returns a timer object that can be used to check if the given
            amount of seconds has passed.
        """

        return Timer(seconds_to_go)

    def check_timer(self, timer):
        """
            Checks if given timer objects has timed out. Cannot be used again,
            unless .reset() is called on the timer.
        """

        return time.time() >= timer._target
