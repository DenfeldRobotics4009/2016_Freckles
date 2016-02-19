__author__ = "nikolojedison"

from wpilib.command import Command

class SetTiltSetpoint(Command):

    def __init__(self, robot, setpoint):
        super().__init__()
        self.robot = robot
        self.setTimeout(3)
        self.setpoint = setpoint
        self.requires(self.robot.tilt)

    def initialize(self):
        self.robot.tilt.enable()
        self.robot.tilt.setSetpoint(self.setpoint)

    def isFinished(self):
        return self.robot.tilt.onTarget() or self.isTimedOut()

    def end(self):
        self.robot.tilt.disable()

    def interrupted(self):
        self.end()
