__author__ = "auxiliary-character"

import csv

import wpilib
from wpilib.command import Command
from wpilib.timer import Timer

from utilities.settings import Settings

class PlayMacro(Command):
    """This plays macro movements from the .csv file."""
    def __init__(self, robot, name):
        """Initialize the command and get all the requirements."""

        super().__init__()
        self.robot = robot
        self.requires(robot.drivetrain)
        self.requires(robot.ears)
        self.requires(robot.hat)
        self.requires(robot.tilt)
        self.name = name
        self.done_yet = False

    def initialize(self):
        """Figure out the file location and play it back."""
        print("Initializing macro " + self.name + "...")

        try:
            #attempt to access the files required
            if self.robot.isReal():
                self.f = open("/home/lvuser/py/macros/"+self.name)
            else:
                self.f = open(self.name)
            self.reader_iterator = csv.DictReader(self.f)
        except FileNotFoundError:
            #This bit runs if the file isn't there
            self.reader_iterator = []

        #length of time to play the macro.
        self.setTimeout(Settings.num_macro_timeout)

        #start time is important for making sure everything plays at the right time
        start_time = Timer.getFPGATimestamp()
        #do the actual playback bit
        for line in self.reader_iterator:
            t_delta = float(line["Time"]) - (Timer.getFPGATimestamp()-start_time)
            if t_delta > 0:
                Timer.delay(t_delta)
            #Add subsystems in the following manner:
            #self.robot.subsystem.manualCommand(float(line["Row_Name"]))

            self.robot.drivetrain.driveManual(float(line["Drive_Y"]),
                                            float(line["Drive_Twist"]))
            self.robot.ears.manualSet(float(line["Ears"]))
            self.robot.hat.manualSet(float(line["Hat"]))
            self.robot.tilt.manualSet(float(line["Tilt"]))

            if self.isTimedOut() or self.done_yet:
                break

    def execute(self):
        pass

    def isFinished(self):
        return True

    def end(self):
        """Run when called, end the macro playing."""

        #set the motors to 0 for safety's sake:
        self.robot.drivetrain.driveManual(0,0)
        self.robot.ears.manualSet(0)
        self.robot.hat.manualSet(0)
        self.robot.tilt.manualSet(0)
        print("Macro playback complete")

        if hasattr(self, "f"):
            self.f.close()

    def interrupted(self):
        """Runs when macro playback is interrupted."""
        self.end()

    def cancel(self):
        """Runs when macro playback is canceled."""

        self.robot.drivetrain.driveManual(0,0)
        self.robot.ears.manualSet(0)
        self.robot.hat.manualSet(0)
        self.robot.tilt.manualSet(0)
        print("Macro playback canceled for the macro " + self.name)
        super().cancel()
