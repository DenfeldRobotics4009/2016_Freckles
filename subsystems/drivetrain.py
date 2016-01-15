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

        self.zed = wpilib.CANTalon(0)
        self.one = wpilib.CANTalon(1)
        self.two = wpilib.CANTalon(2)
        self.three = wpilib.CANTalon(3)
        self.four = wpilib.CANTalon(4)
        self.five = wpilib.CANTalon(5)
        self.six = wpilib.CANTalon(6)
        self.seven = wpilib.CANTalon(7)

        self.firstSet = wpilib.RobotDrive()
        self.secondSet = wpilib.RobotDrive()
        self.thirdSet = wpilib.RobotDrive()
        self.fourthSet = wpilib.RobotDrive()

    def initDefaultCommand(self):
        self.setDefaultCommand(DriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):
        precision = True
        x = drive_control(-joystick.getX()*2, precision)
        y = drive_control(-joystick.getY()*2, precision)
        z = precision_mode(dead_zone(joystick.getRawAxis(3), .1), precision)
        if x>1:
            x=1
        elif x<-1:
            x=-1
        self.driveManual(x,y,z)

    def driveManual(self, x, y, rotation):
        self.x, self.y, self.rotation = x, y, rotation
        self.firstSet
