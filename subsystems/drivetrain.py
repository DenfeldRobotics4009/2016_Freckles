__author__ = "nikolojedison"

import math

import wpilib
from wpilib.command import Subsystem

from utilities.drive_control import *
from utilities.settings import Settings
from oi import OI

from commands.manual.power_of_the_friendship import DriveWithJoystick

class Drivetrain(Subsystem):

    def __init__(self, robot):

        super().__init__()
        self.robot = robot
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.joystick = wpilib.Joystick(0)

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

        two = drive_control(-self.joystick.getRawAxis(2), self.joystick.getButton(0), self.joystick.getButton(1))*1.5
        y = drive_control(-self.joystick.getY(), self.joystick.getButton(0), self.joystick.getButton(1))*2.5

        if two>1:
            two=1
        elif two<-1:
            two=-1
        self.driveManual(y,two)

    def driveManual(self, y, two):
        self.y, self.two = y, two

        self.firstSet.arcadeDrive(y, two)
        self.secondSet.arcadeDrive(y, two)
        self.thirdSet.arcadeDrive(y, two)
