__author__ = "nikolojedison"

import wpilib
from wpilib.command import PIDSubsystem
from commands.manual.manual_tilt import ManualTilt
from utilities.settings import Settings

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
        wpilib.SmartDashboard.putNumber("Tilt Pot", self.tilt_pot.get()) #publish the tilt value to the dash

    def manualSet(self, output):
        position = self.tilt_pot.get()
        if position < utilities.settings.kDown:
            self.tilt_motor.set(0)
        elif position > utilities.settings.kUp:
            self.tilt_motor.set(0)
        else:
            self.tilt_motor.set(output)


    def returnPIDInput(self):
        return self.tilt_pot.get()

    def usePIDOutput(self, output):
        self.manualSet(output)

    def isDown(self):
        self.tilt_pot.get() < utilities.settings.kDown

    def isUp(self):
        return not self.isDown()
