__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.hat import Hat

class HatButton(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.hat)
        self.speed = speed

    def execute(self):
        self.robot.hat.manualSet(self.speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.hat.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
