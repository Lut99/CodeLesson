# BAL.py
#   by Lut99
#
# Dit bestand bevat de class voor de Bal. Het is een derived class van
#   GameObject, en bedoeld om te worden bewogen in de puzzel. Daarnaast
#   is er ook de Programma subclass van de Robot, die gebruikt wordt om hem
#   te programmeren.

import threading
import pygame

from GameBase.GameObject import GameObject
from GameBase.Sprite import Sprite
from GameBase.GameTime import Timer


class ProgramError(Exception):
    pass


class Program:
    """
        The program class is an interface to the robot that is used in the
        puzzel file. Upon calling an instruction, the instruction passes this
        to the robot object and waits until the waiting time has passed before
        continuing.
    """

    NOORD = "noord"
    OOST = "oost"
    ZUID = "zuid"
    WEST = "west"
    BOVEN = "boven"
    RECHTS = "rechts"
    ONDER = "onder"
    LINKS = "links"

    def __init__(self):
        self.to_execute = None
        self.state = "waiting"
        self.result = None

    def stap(self, amount=1):
        """
            Makes the robot walk amount steps in the direction he is pointing
            at at the moment.
        """

        # Wait until we're idle
        while self.state != "idle":
            pass

        # Check if int
        if type(amount) == int and amount >= 0:
            for i in range(amount):
                # Wait until we're idle

                # Set the to be executed program
                self.to_execute = tuple(["step"])

                # Update the state
                self.state = "executing"

                # Wait until we're idle
                while self.state != "idle":
                    pass
        else:
            self.to_execute = ("error", "robot.stap(): Het aantal stappen moet een geheel, positief getal zijn")
            self.state = "executing"
            raise ProgramError()

    def draai(self, direction):
        """
            Turns the robot a relative amount to what it is rotated now from.
            Can enter either: 'links' or 'rechts'.
        """

        # Wait until we're idle
        while self.state != "idle":
            pass

        # Either do the instruction or print an error
        if direction in ["links", "rechts"]:
            self.to_execute = ("turn", direction)
            self.state = "executing"
        else:
            self.to_execute = ("error", f"robot.draai(): Onbekende richting '{direction}'")
            self.state = "executing"
            raise ProgramError()

        # Wait until we're idle
        while self.state != "idle":
            pass

    def draai_kompas(self, direction):
        """
            Turns the robot to the specified direction. This is absolute, not
            relative to the current rotation. Rotation values are: 'noord',
            'oost', 'zuid' or 'west'.
        """

        # Wait until we're idle
        while self.state != "idle":
            pass

        # Either do the instruction or print an error
        if direction in ["noord", "oost", "zuid", "west"]:
            self.to_execute = ("turn_compass", direction)
            self.state = "executing"
        else:
            self.to_execute = ("error", f"robot.draai_kompas(): Onbekende richting '{direction}'")
            self.state = "executing"
            raise ProgramError()

        # Wait until we're idle
        while self.state != "idle":
            pass

    def kijk(self):
        """
            Geeft terug wat er voor de robot staat.
        """

        # Wait until we're idle
        while self.state != "idle":
            pass

        # Set the instruction, then wait for idle to return
        self.to_execute = tuple(["look"])
        self.state = "executing"

        while self.state != "idle":
            pass

        return self.result


class ExecutionThread(threading.Thread):
    """
        The ExecutionThread runs the robot program detached from the main
        program. It's biggest job is relaying the information stored in the
        program (actions) and relaying those back to the robot. Additionally,
        it can also request information (such as in kijk()). Note that every-
        thing is handle
    """

    def __init__(self, program, func):
        threading.Thread.__init__(self, daemon=True)

        self.running = False

        self._to_exec = func
        self._program = program

    def run(self):
        self.running = True

        try:
            self._to_exec(self._program)
        except ProgramError:
            # Hides the actual traceback and stuff
            pass

        self.running = False


# Represents the Robot (player)
class Robot(GameObject):
    def __init__(self, program, level, pos=(0, 0), rotation="oost"):
        super().__init__("Robot", (0, 0, 75, 75), sprite=Sprite("GameObjects/sprites/robot1.png"), rotation=rotation, crossable=False)

        self._level = level

        # Create a program
        self._program_host = Program()

        # Create the thread
        execution = ExecutionThread(self._program_host, program)

        # Run it
        execution.start()

        # Declare the second timer
        self._timer = Timer(1)

        # Text ballon visibility indicator
        self.show_text = None
        self.font = pygame.font.SysFont("Ariel", 24)

    def update(self, gametime):

        # Check if there is some command scheduled
        if self._program_host.state == "executing":
            # Execute the given instruction
            command = self._program_host.to_execute[0]

            if command == "step":
                clipped = self._level.move(self, self.rotation)
                if clipped:
                    # Show a textbox
                    self.talk("Obstakel!")
            elif command == "turn":
                # Add our direction to the current one
                if self._program_host.to_execute[0] == "links":
                    # Turn left
                    directions = ["noord", "west", "zuid", "oost"]
                    self.rotation = directions[(directions.index(self.rotation) + 1) % len(directions)]
                else:
                    # Turn right
                    directions = ["noord", "oost", "zuid", "west"]
                    self.rotation = directions[(directions.index(self.rotation) + 1) % len(directions)]
            elif command == "turn_compass":
                # Turn to the given direction
                self.rotation = self._program_host.to_execute[1]
            elif command == "look":
                # Compute grid coordinates of what is in front of us
                x = int(self.x / self._level.grid_size)
                y = int(self.y / self._level.grid_size)
                if self.rotation == "noord":
                    y -= 1
                elif self.rotation == "oost":
                    x += 1
                elif self.rotation == "zuid":
                    y += 1
                elif self.rotation == "west":
                    x -= 1

                # Get what is in front of us, then return that in the return var
                obj = self._level.get(x, y)
                if obj == "OutOfBounds":
                    self.talk("Ik zie: Rand")
                    self._program_host.result = obj
                elif obj == "Air":
                    self.talk("Ik zie: Niks")
                    self._program_host.result = obj
                else:
                    self.talk(f"Ik zie: {obj.name}")
                    self._program_host.result = obj.name
            elif command == "error":
                # Display the error so the kids know something is up, and
                #   freeze the timer. The Program thread should have killed
                #   itself.
                self.talk("ERROR")
                print(f"ERROR: {self._program_host.to_execute[1]}")
                self._timer.stop()

            # Set it to waiting
            self._program_host.state = "waiting"
        elif self._program_host.state == "waiting":
            # Check if a second has passed
            if gametime.check_timer(self._timer):
                self._program_host.state = "idle"
                # Also reset any text boxes
                self.show_text = None
                # And reset the timer
                self._timer.reset()

        # Propagate the position once all changes have been made
        super().update(gametime, (self.x, self.y, self.w, self.h), self.rotation)

    def draw(self, screen):
        # Draw the robot first
        super().draw(screen)

        # If needed, also draw the textbox
        if self.show_text is not None:
            # Determine if we should draw up or below the robot
            w, h = self.font.size(self.show_text)
            up_left = (self.x + (self.w * 0.5) - (w / 2) - 10, self.y - h - 20)
            if up_left[1] < 0:
                up_left = (self.x + (self.w * 0.5) - (w / 2) - 10, self.y + self.h)
            
            # Also check if X is out-of-bounds
            if up_left[0] < 0:
                up_left = (0, up_left[1])
            if up_left[0] + w + 20 > screen.get_size()[0]:
                up_left[0] = screen.get_size()[0] - w - 20

            # Draw the rectangle
            pygame.draw.rect(screen, (255, 255, 255), (up_left[0], up_left[1], w + 20, h + 20))
            pygame.draw.rect(screen, (0, 0, 0), (up_left[0], up_left[1], w + 20, h + 20), 2)

            # Draw the text in the center
            screen.blit(self.font.render(self.show_text, False, (0, 0, 0)), (up_left[0] + 10, up_left[1] + 10))

    def talk(self, text):
        """
            Let's the robot say something. Will spawn a textbox above the
            robot, unless it's out of bounds of the screen, in which case
            it will be shown below the robot.
        """

        self.show_text = text
