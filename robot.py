#!/usr/bin/env python3
__author__ = "nikolojedison"

import wpilib
from wpilib.command import Scheduler
import networktables

from utilities.settings import Settings

from subsystems.drivetrain import Drivetrain

from oi import OI

class Freckles(wpilib.SampleRobot):
    """Fluffy ears to scratch, lost his tail, cute little paws, likes to play fetch."""

    def robotInit(self):

        self.drivetrain = Drivetrain(self)
        self.oi = OI(self)
        self.sensitivity = self.oi.smart_dashboard.getInt("Sensitivity", 5)
        self.macroTimeout = self.oi.smart_dashboard.getInt("Macro", 15)
        Settings.num_macro_timeout = self.macroTimeout

    def autonomous(self):

        #Logging loop
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        joystick = self.oi.getStick()

        #Sensitivity settings structure. Gets the sensitivity value from the
        #smart dashboard (returning 5 as the default), and adjust the
        #corresponding values accordingly.
        try:
            if self.sensitivity == 1:
                Settings.num_scaling = 0.10
                Settings.num_drive = 5
            elif self.sensitivity == 2:
                Settings.num_scaling = 0.25
                Settings.num_drive = 4
            elif self.sensitivity == 3:
                Settings.num_scaling = 0.45
                Settings.num_drive = 4
            elif self.sensitivity == 4:
                Settings.num_scaling = 0.60
                Settings.num_drive = 4
            elif self.sensitivity == 5:
                Settings.num_scaling = 0.75
                Settings.num_drive = 4
            elif self.sensitivity == 6:
                Settings.num_scaling = 1.25
                Settings.num_drive = 3
            elif self.sensitivity == 7:
                Settings.num_scaling = 1.5
                Settings.num_drive = 3
            elif self.sensitivity == 8:
                Settings.num_scaling = 1.85
                Settings.num_drive = 3
            elif self.sensitivity == 9:
                Settings.num_scaling = 2.3
                Settings.num_drive = 2
            else:
                Settings.num_scaling = 0.75
                Settings.num_drive = 4

        except KeyError:
                Settings.num_scaling = 0.75
                Settings.num_drive = 4

        #Logging loop
        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)

    def disabled(self):

        #Stop the drivetrain for safety's sake.
        self.drivetrain.driveManual(0,0)

        #Logging loop
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005)

    def test(self):
        pass

    def log(self):
        """I know it doesn't log but if it does eventually it'll go here"""
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(Freckles)
