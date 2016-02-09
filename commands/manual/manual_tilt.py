__author__ = "nikolojedison"

from wpilib.command import command
from drive_control import dead_zone
import utilities.settings

class ManualTilt(Command):
    """Manually tilt the ears."""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.tilt)

        def execute(self):
            self.robot.tilt.manualSet(self.robot.oi.getStick.getZ(self))

        def isFinished(self):
            return False

        def cancel(self):
            self.robot.tilt.manualSet(0)
            super.cancel()
