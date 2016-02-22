#!/usr/bin/env python3
__author__ = "nikolojedison"

#Import robot-specific libraries:
import wpilib
from wpilib.command import Scheduler
import networktables

#Import our robot-specific libraries:
from utilities.settings import Settings

#Import our subsystems:
from subsystems.drivetrain import Drivetrain
from subsystems.hat import Hat
from subsystems.ears import Ears
from subsystems.tilt import Tilt

#Import our button mapping:
from oi import OI

#Import our commands:
from macros.play_macro import PlayMacro

class Mantis(wpilib.SampleRobot):
    """Fluffy ears to scratch, lost his tail, cute little paws, likes to play fetch."""

    def robotInit(self):
        """Initialise the robot."""

        #Initialise the subsystems and the button mapping:
        self.drivetrain = Drivetrain(self)
        self.ears = Ears(self)
        self.hat = Hat(self)
        self.tilt = Tilt(self)
        self.oi = OI(self)

        self.macroTimeout = self.oi.smart_dashboard.getInt("Macro", 15)
        Settings.num_macro_timeout = 15

    def autonomous(self):
        """Auton code."""

        #Change when we get to something useful.

        #Logging loop
        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def operatorControl(self):
        """Teleop code."""
        #Make the joystick work for driving:
        joystick = self.oi.getStick()

        #Logging loop
        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def disabled(self):
        """Code to run when disabled."""

        #Stop the drivetrain for safety's sake:
        self.drivetrain.driveManual(0,0)
        self.hat.manualSet(0)
        self.ears.manualSet(0)
        self.tilt.manualSet(0)

        #Logging loop
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def test(self):
        """Code for testing."""
        pass

    def log(self):
        """I know it doesn't log but if it does eventually it'll go here."""
        #Log the things:
        self.drivetrain.log()
        self.ears.log()
        self.hat.log()
        self.tilt.log()

if __name__ == "__main__":
    wpilib.run(Mantis)
