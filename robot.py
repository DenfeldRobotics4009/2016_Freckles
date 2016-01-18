#!/usr/bin/env python3
__author__ = "nikolojedison"

import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

from subsystems.drivetrain import Drivetrain

class Freckles(wpilib.SampleRobot):
    """Fluffy ears to scratch, lost his tail, cute little paws, likes to play fetch."""

    def robotInit(self):
        self.drivetrain = Drivetrain(self)
        self.oi = OI(self)
        self.sensitivity = self.oi.smart_dashboard.getInt("Sensitivity", 5)

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        joystick = self.oi.getStick()
        try:
            if self.sensitivity == 1:
                pass
            elif self.sensitivity == 2:
                pass
            elif self.sensitivity == 3:
                pass
            elif self.sensitivity == 4:
                pass
            elif self.sensitivity == 5:
                pass
            elif self.sensitivity == 6:
                pass
            elif self.sensitivity == 7:
                pass
            elif self.sensitivity == 8:
                pass
            elif self.sensitivity == 9:
                pass
            else:
                pass
        except KeyError:
                pass

        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005)

    def disabled(self):
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005)

    def test(self):
        pass

    def log(self):
        self.drivetrain.log() #I know it doesn't log but if it does eventually it'll go here

if __name__ == "__main__":
    wpilib.run(Freckles)
