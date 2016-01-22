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
        self.five.set(0)
        self.one.set(0)
        self.four.set(0)
        self.three.set(0)
        self.two.set(0)
        self.zed.set(0)

        if x > 0.0625 or x < -0.0625 :
            self.five.set(x)
            self.one.set(x)
            self.four.set(x)
            self.three.set(x)
            self.two.set(x)
            self.zed.set(x)

        elif y > 0.0625 or y < -0.0625:
            self.four.set(y)
            self.one.set(y)
            self.five.set(y)
            self.three.set(y)
            self.two.set(y)
            self.zed.set(y)

        else:
            self.zed.set(0)
            self.one.set(0)
            self.two.set(0)
            self.three.set(0)
            self.four.set(0)
            self.five.set(0)
