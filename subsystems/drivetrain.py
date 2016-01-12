
__author__ = "nikolojedison"
import math

import wpilib
from wpilib.command import Subsystem
from drive_control import *
from imu_simple import IMUSimple

class Drivetrain(Subsystem):

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

    def initDefaultCommand(self):
        self.setDefaultCommand(MecanumDriveWithJoystick(self.robot))

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
        self.drive.mecanumDrive_Cartesian(x, y, rotation, 0)
