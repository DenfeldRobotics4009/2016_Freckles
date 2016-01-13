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

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005)

    def operatorControl(self):
        joystick = self.oi.getStick()

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
        pass

if __name__ == "__main__":
    wpilib.run(Freckles)
