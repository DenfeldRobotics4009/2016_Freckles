__author__ = "nikolojedison"

import wpilib
from wpilib.command import Subsystem

from utilities.settings import Settings
from oi import OI

from commands.manual.wiggle_toes import WiggleToes

class Toes(Subsystem):
    def __init__(self, robot):

        self.robot = robot

        self.toeLeft = wpilib.CANTalon(9)
        self.toeRight = wpilib.CANTalon(2)

    def initDefaultCommand(self):
        selfsetDefaultCommand(WiggleToes(self.robot))

    def manualSet(self, output):
        self.toeLeft.set(output)
        self.toeRight.set(output)

    def log(self):
        pass
