__author__ = "nikolojedison"

import math

import wpilib
from wpilib.command import Subsystem

from utilities.drive_control import *
from utilities.settings import Settings

from commands.manual.power_of_the_friendship import DriveWithJoystick

class Drivetrain(Subsystem):

    def __init__(self, robot):

        super().__init__()
        self.robot = robot
        self.x = 0
        self.y = 0
        self.rotation = 0

        #CANTalon motors for the drivetrain.
        self.zed = wpilib.CANTalon(0)
        self.one = wpilib.CANTalon(1)
        self.two = wpilib.CANTalon(2)
        self.three = wpilib.CANTalon(3)
        self.four = wpilib.CANTalon(4)
        self.five = wpilib.CANTalon(5)

        #Actual drivetrains. Basically fun.
        self.firstSet = wpilib.RobotDrive(self.zed, self.one)
        self.secondSet = wpilib.RobotDrive(self.two, self.three)
        self.thirdSet = wpilib.RobotDrive(self.four, self.five)

    def initDefaultCommand(self):
        self.setDefaultCommand(DriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):

        precision = False

        y = drive_control(-joystick.getRawAxis(2))
        x = drive_control(-joystick.getY())

        if x>1:
            x=1
        elif x<-1:
            x=-1
        self.driveManual(x,y)

    def driveManual(self, x, y):

        self.x, self.y = x, y

        self.firstSet.arcadeDrive(x, y)
        self.secondSet.arcadeDrive(x, y)
        self.thirdSet.arcadeDrive(x, y)
