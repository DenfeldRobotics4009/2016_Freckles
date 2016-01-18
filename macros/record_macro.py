__author__ = "auxiliary-character"

import csv

import wpilib
from wpilib.command import Command
from wpilib.timer import Timer

from utilities.settings import Settings

class RecordMacro(Command):
    """This records robot movements and writes them to a .csv file."""
    def __init__(self, robot, name):

        super().__init__()
        self.robot = robot

        #length of time to record the macro.
        self.setTimeout(Settings.num_macro_timeout)

        self.name = name

    def initialize(self):

        self.initTime = wpilib.Timer.getFPGATimestamp() #get the current time
        self.f = open("/home/lvuser/py/macros/"+self.name, "w")
        fields = ["Drive_X",
                  "Drive_Y",]
        self.writer = csv.DictWriter(self.f, fieldnames=fields)
        self.writer.writeheader()

    def execute(self):

        self.writer.writerow({
            "Drive_X": self.robot.drivetrain.x,
            "Drive_Y": self.robot.drivetrain.y,

            #this is needed to make sure everything runs at the right time, v. important:
            "Time": wpilib.Timer.getFPGATimestamp() - self.initTime}) #get the time as the row is written

    def isFinished(self):
        return self.isTimedOut()

    def end(self):
        self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):

        self.end()
        super().cancel()
