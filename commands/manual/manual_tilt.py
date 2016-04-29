__author__ = "nikolojedison"

from wpilib.command import Command
import utilities.settings
from utilities.drive_control import *
from utilities.drive_control import dead_zone

class ManualTilt(Command):
    """Manually tilt the ears."""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.tilt)
        self.joystick = wpilib.Joystick(0)

    def execute(self):
        joystick = self.joystick
        precision = False
        self.robot.tilt.manualSet(dead_zone(tilt_control(self.robot.oi.getSetpointStick().getRawAxis(1), self.robot.oi.getSetpointStick().getRawButton(2)), .40))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.tilt.manualSet(0)
        super().cancel()
