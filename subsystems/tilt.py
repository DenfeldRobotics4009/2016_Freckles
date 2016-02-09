__author__ = "nikolojedison"

import wpilib
from wpilib.command import PIDSubsystem
from commands.manual.manual_tilt import ManualTilt
from utilities.settings import Settings

class Tilt(PIDSubsystem):
    """The tilting mechanism for the shooter."""

    def  __init__(self, robot):
        super().__init__(20, 0, 0)

        #We need 1 motor and 1 potentiometer.

        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualTilt(self.robot))

    def log(self):
        #Send the value from the potentiometer you defined in __init__ to the
        # drive station.

    def manualSet(self, output):
        #Set your motor to  "output"

    def returnPIDInput(self):
        #Put the value from the potentiometer you defined in __init__.

    def usePIDOutput(self, output):
        self.manualSet(output)
