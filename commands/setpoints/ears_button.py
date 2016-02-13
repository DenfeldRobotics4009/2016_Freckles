__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.ears import Ears

class EarsButton(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.ears)
        self.speed = speed

    def execute(self):
        self.robot.ears.manualSet(self.speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.ears.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
