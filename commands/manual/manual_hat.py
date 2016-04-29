__author__ = "nikolojedison"

from wpilib.command import Command

class ManualHat(Command):
    """Manually run the trigger wheel."""

    def __init__(self, robot, output):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.hat)

    def execute(self, output):
        pass

    def isFinished(self):
        return self.isTimedOut()

    def cancel(self):
        self.robot.hat.manualSet(0)
        super().cancel()
