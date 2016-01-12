__author__ = 'nikolojedison'

from wpilib.command import command

class FrecklesDrive(Command):

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)

    def execute(self):
        self.robot.drivetrain.driveJoystick(self.robot.oi.getStick())

    def isFinished(self):
        return False

    def end(self):
        self.robot.drivetrain.driveManual(0,0,0)
        pass

    def interrupted(self):
        self.end()
