__author__ = "nikolojedison"

import wpilib
from wpilib.command import Subsystem
from utilities.settings import Settings
from commands.manual.manual_hat import ManualHat

class Hat(Subsystem):
    """Run the trigger wheel."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.motor = wpilib.CANTalon(1)

    def initDefaultCommand(self):
        self.setDefaultCommand

    def manualSet(self, output):
        self.motor.set(output)

    def log(self):
        pass
