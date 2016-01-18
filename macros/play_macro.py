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
        self.name = name
        self.done_yet = False

    def initialize(self):

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

        for line in self.reader_iterator:
            t_delta = float(line["Time"]) - (Timer.getFPGATimestamp()-start_time)
            if t_delta > 0:
                Timer.delay(t_delta)
            self.robot.drivetrain.driveManual(float(line["Drive_X"]),
                                            float(line["Drive_Y"]), 0)
            if self.isTimedOut() or self.done_yet:
                break

    def execute(self):
        pass

    def isFinished(self):
        return True

    def end(self):
        #set the motors to 0 for safety's sake:

        self.robot.drivetrain.driveManual(0,0,0)
        if hasattr(self, "f"):
            self.f.close()

    def interrupted(self):
        self.end()

    def cancel(self):

        self.end()
        super().cancel()
