__author__ = "nikolojedison"

from wpilib.command import Command

class ManualTrigger(Command):
    """Manually run the trigger spool."""

    def __init__(self, robot, output):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.trigger_wheel)

    def execute(self, output):
        self.robot.trigger_wheel.manualSet(self.robot.oi.getStick().getRawAxis(4), output)

    def isFinished(self):
        return False

    def cancel(self):
        self.robot.trigger_wheel.manualSet(0)
        super().cancel()
