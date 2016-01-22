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

        #Timeout value for the macros from the dashboard (default 15 sec)
        self.macroTimeout = self.oi.smart_dashboard.getInt("Macro", 15)
        Settings.num_macro_timeout = self.macroTimeout

    def autonomous(self):

        #Logging loop
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def operatorControl(self):
        joystick = self.oi.getStick()

        #Logging loop
        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def disabled(self):

        #Stop the drivetrain for safety's sake.
        self.drivetrain.driveManual(0,0)

        #Logging loop
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def test(self):
        pass

    def log(self):
        """I know it doesn't log but if it does eventually it'll go here"""
        self.drivetrain.log()

if __name__ == "__main__":
    wpilib.run(Freckles)
