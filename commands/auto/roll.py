__author__ = "nikolojedison"

from wpilib.command import Command

class Roll(Command):
    """Roll the ball for the shoot command."""

    def __init__(self, robot, output, timeout):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.hat)
        self.setTimeout(timeout)
        self.output = output

    def execute(self):
        self.robot.hat.manualSet(self.output)

    def isFinished(self):
        return self.isTimedOut

    def cancel(self):
        self.robot.hat.manualSet(0)
        super().cancel()
