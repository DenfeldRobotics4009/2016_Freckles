
__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem
from commands.manual.power_of_the_friendship import DriveWithJoystick
from utilities.drive_control import *

class Drivetrain(Subsystem):

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.x = 0
        self.y = 0
        self.rotation = 0

        self.zed = wpilib.Talon(0)
        self.one = wpilib.Talon(1)

        self.drive = wpilib.RobotDrive(self.zed, self.one)

    def initDefaultCommand(self):
        self.setDefaultCommand(DriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):
        precision = True
        x = drive_control(joystick.getX(), precision)
        y = drive_control(joystick.getY(), precision)
        z = precision_mode(dead_zone(joystick.getRawAxis(3), .1), precision)
        if x>1:
            x=1
        elif x<-1:
            x=-1
        self.driveManual(x,y,z)

    def driveManual(self, x, y, rotation):
        self.x, self.y, self.rotation = x, y, rotation
        self.drive.arcadeDrive(x, y, rotation)
