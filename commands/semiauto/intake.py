__author__ = "nikolojedison"

from wpilib.command import Command

from commands.manual.manual_trigger import ManualTrigger
from commands.manual.manual_ears import ManualEars

class Intake(Command):
    """Run the ear spools alongside the trigger to intake a ball."""

    def __init__(self, robot):
        super().__init__()
        self.spool_command = ManualEars(robot, 1)
        self.trigger_command = ManualTrigger(robot, 1)

    def initialize(self):
        self.spool_command.start()
        self.trigger_command.start()

    def execute(self):
        self.spool_command.start()
        self.trigger_command.start()

    def cancel(self):
        self.spool_command.cancel()
        self.trigger_command.cancel()
        super().cancel()

    def isFinished(self):
        return False
