__author__ = "nikolojedison"

from wpilib.command import Command
import utilities.settings

class ManualTilt(Command):
    """Manually tilt the ears."""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.tilt)

    def execute(self):
        self.robot.tilt.manualSet(self.robot.oi.getStick().getRawAxis(2))

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.tilt.manualSet(0)
        super.cancel()
