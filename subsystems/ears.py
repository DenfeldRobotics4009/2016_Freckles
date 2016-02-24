__author__ = "nikolojedison"

import wpilib
from wpilib.command import Subsystem
from utilities.settings import Settings
from commands.manual.manual_ears import ManualEars

class Ears(Subsystem):
    """Run the ear spools."""

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.left = wpilib.CANTalon(6)
        self.right = wpilib.CANTalon(8)
        self.loaded = wpilib.DigitalInput(2)

    def initDefaultCommand(self):
        self.setDefaultCommand

    def manualSet(self, output):
        self.left.set(-output)
        self.right.set(output)

    def log(self):
        wpilib.SmartDashboard.putBoolean("Ball Limit", self.loaded.get())
