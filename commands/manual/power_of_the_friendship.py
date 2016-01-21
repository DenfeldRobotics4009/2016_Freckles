__author__ = "nikolojedison"

from wpilib.command import Command

class DriveWithJoystick(Command):

    def __init__(self, robot):

        super().__init__()
        self.robot = robot
        self.requires(self.robot.drivetrain)

    def execute(self):
        self.robot.drivetrain.driveJoystick(self.robot.oi.getStick())

    def isFinished(self):
        #keep the robot from running the driveJoystick command once then dying:
        return False

    def end(self):

        #Set the drivetrain values to 0 so the robot stops:
        self.robot.drivetrain.driveManual(0,0)
        pass

    def interrupted(self):
        #If interrupted (could do logs here):
        self.end()
