__author__ = "nikolojedison"

import math

import wpilib
from wpilib.command import Subsystem

from utilities.pov_button import POVButton
from utilities.drive_control import *
from utilities.settings import Settings
from oi import OI

from commands.manual.power_of_the_friendship import DriveWithJoystick

class Drivetrain(Subsystem):

    def __init__(self, robot):
        """Initialise the drivetrain."""

        super().__init__()
        #Set up everything
        self.robot = robot
        #Set the values to 0 to make sure things work without running away
        self.twist = 0
        self.y = 0
        #0-indexed joysticks lol
        self.joystick = wpilib.Joystick(0)

        #CANTalon motors for the drivetrain.
        self.zed = wpilib.CANTalon(9)
        self.one = wpilib.CANTalon(2)
        self.two = wpilib.CANTalon(3)
        self.three = wpilib.CANTalon(7)
        self.four = wpilib.CANTalon(5)
        self.five = wpilib.CANTalon(4)

        #Actual drivetrains. Basically fun.
        self.firstSet = wpilib.RobotDrive(self.zed, self.one)
        self.secondSet = wpilib.RobotDrive(self.two, self.three)
        self.thirdSet = wpilib.RobotDrive(self.four, self.five)
        print("Drivetrain initialized")

    def initDefaultCommand(self):
        """Set the DriveWithJoystick command to run so the drivetrain will move."""
        self.setDefaultCommand(DriveWithJoystick(self.robot))

    def log(self):
        pass

    def driveJoystick(self, joystick):
        """Get the values from the joystick, and pass them to the driveManual function."""

        #Set precision to be false so the drivetrain isn't auto-nerfed
        precision = False

        #                      /-twist joystick              /-1st precision button        /-multiplier so it goes to 1
        twist = dead_zone(twist_control(-self.joystick.getRawAxis(2), self.joystick.getRawButton(1))*5, .25)
        y = dead_zone(drive_control(-self.joystick.getRawAxis(1), self.joystick.getRawButton(1))*2.5, .25)
        #                  \-main forward joystick \-1st precision button               \-multiplier so it goes to 1

        #what even is this
        if twist>1:
            twist=1
        elif twist<-1:
            twist=-1

        self.driveManual(y, twist)

    def driveManual(self, y, twist):
        """Pass the values from driveJoystick to the actual drivetrain sets."""

        #Assign the proper values that we set up earlier
        self.y, self.twist = y, twist

        self.firstSet.arcadeDrive(y, twist)
        self.secondSet.arcadeDrive(y, twist)
        self.thirdSet.arcadeDrive(y, twist)
