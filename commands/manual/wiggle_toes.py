__author__ = "nikolojedison"

from wpilib.command import Command

class WiggleToes(Command):
    """Move the front-end toe wheels"""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.toes = self.robot.toes

    def execute(self):
        pass

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.toes.manualSet(0)
        super().cancel()
