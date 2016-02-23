__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointShootLevel(SetTiltSetpoint):
    """Fire at the setpoint."""
    def __init__(self, robot):
        super().__init__(robot, Settings.kShootLevel)

    def isFinished(self):
        return super().isFinished()
