__author__ = "nikolojedison"
from wpilib.command import Command
from subsystems.ears import Ears
from subsystems.hat import Hat

class Intake(Command):
    def __init__(self, robot, ear_speed, hat_speed):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.ears)
        self.ear_speed = ear_speed
        self.hat_speed = hat_speed

    def execute(self):
        self.robot.ears.manualSet(self.ear_speed)
        self.robot.hat.manualSet(self.hat_speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.ears.manualSet(0)
        self.robot.hat.manualSet(0)

    def cancel(self):
        self.end()
        super().cancel()
