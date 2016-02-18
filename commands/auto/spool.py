__author__ = "nikolojedison"

from wpilib.command import Command

class Spool(Command):
    """Run the ear spools for the shoot command."""

    def __init__(self, robot, output, timeout):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.ears)
        self.setTimeout(timeout)
        self.output = output

    def execute(self):
        self.robot.ears.manualSet(self.output)

    def isFinished(self):
        return self.isTimedOut

    def cancel(self):
        self.robot.ears.manualSet(0)
        super().cancel()
