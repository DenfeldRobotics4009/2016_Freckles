__author__ = "auxiliary-character"

import csv

import wpilib
from wpilib.command import Command
from wpilib.timer import Timer

from utilities.settings import Settings

class RecordMacro(Command):
    """This records robot movements and writes them to a .csv file."""
    def __init__(self, robot):

        super().__init__()
        self.robot = robot

        #length of time to record the macro.
        self.setTimeout(Settings.num_macro_timeout)
        self.name = Settings.str_macro_name

    def initialize(self):
        """Set up the macro file and prepare for recording."""
        print("Initializing macro " + self.name + "...")

        self.initTime = wpilib.Timer.getFPGATimestamp() #get the current time
        self.f = open("/home/lvuser/py/macros/"+self.name, "w")
        fields = ["Drive_Y",
                  "Drive_Twist",
                  "Ears",
                  "Hat",
                  "Tilt",
                  "Time"]
        self.writer = csv.DictWriter(self.f, fieldnames=fields)
        self.writer.writeheader()

    def execute(self):
        """Record the macro."""

        print("Recording macro...")
        #do the actual writing bit:
        self.writer.writerow({
            #Add subsystems in the following manner:
            #"Row_Name": self.robot.subsystem.getValue
            "Drive_Y": self.robot.drivetrain.y,
            "Drive_Twist": self.robot.drivetrain.twist,
            "Ears": self.robot.ears.motor.get(),
            "Hat": self.robot.hat.motor.get(),
            "Tilt": self.tilt.motor.get(),

            #this is needed to make sure everything runs at the right time, v. important:
            "Time": wpilib.Timer.getFPGATimestamp() - self.initTime}) #get the time as the row is written

    def isFinished(self):
        """Returns .isTimedOut() when called."""
        return self.isTimedOut()

    def end(self):
        """Close out & save the macro when called."""
        self.f.close()
        print("Macro recorded")

    def interrupted(self):
        """Run when macro recording is interrupted."""
        self.end()

    def cancel(self):
        """Run when macro recording is canceled."""

        self.end()
        super().cancel()
