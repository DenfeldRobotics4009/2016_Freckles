__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointShootLevel(SetTiltSetpoint):
    """Move to the setpoint for shooting at the middle of the courtyard on level ground."""
    def __init__(self, robot):
        super().__init__(robot, Settings.kShootLevel)

    def isFinished(self):
        return super().isFinished()
