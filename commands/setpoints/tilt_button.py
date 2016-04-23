__author__ = "nikolojedison"

import wpilib
from wpilib.command import Command
from subsystems.tilt import Tilt

class TiltButton(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.tilt)
        self.tilt_pot = self.robot.tilt.tilt_pot

    def execute(self):
        if self.tilt_pot.getValue() > .411:
            self.robot.tilt.manualSet(.2)
        if self.tilt_pot.getValue() <= .411:
            self.robot.tilt.manualSet(-.2)

    def isFinished(self):
        return False

    def end(self):
        self.robot.hat.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
