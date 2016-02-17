__author__ = "nikolojedison"

import wpilib
from wpilib.command import PIDSubsystem
from commands.manual.manual_tilt import ManualTilt
import utilities.settings

class Tilt(PIDSubsystem):
    """The tilting mechanism for the shooter."""

    def  __init__(self, robot):
        super().__init__(20, 0, 0)

        self.robot = robot
        self.tilt_motor = wpilib.CANTalon(10)
        self.tilt_pot = wpilib.AnalogPotentiometer(0)

        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        self.setDefaultCommand(ManualTilt(self.robot))

    def log(self):
        wpilib.SmartDashboard.putNumber("Tilt Pot", self.tilt_pot.get()) 

    def manualSet(self, output):
        position = self.tilt_pot.get()
        if position < utilities.settings.kMaxDown:
            self.tilt_motor.set(0)
        elif position > utilities.settings.kMaxUp:
            self.tilt_motor.set(0)
        else:
            self.tilt_motor.set(output)


    def returnPIDInput(self):
        return self.tilt_pot.get()

    def usePIDOutput(self, output):
        self.manualSet(output)

    def isDown(self):
        self.tilt_pot.get() < utilities.settings.kMaxDown

    def isUp(self):
        return not self.isDown()
