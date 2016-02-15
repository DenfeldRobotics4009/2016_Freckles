__author__ = "nikolojedison"

from wpilib.command import Command

class ManualEars(Command):
    """Manually run the ear spools."""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.ears)

    def execute(self):
        pass

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.ears.manualSet(0)
        super().cancel()