__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class SetpointTop(SetTiltSetpoint):
    """Fire at the setpoint."""

    def __init__(self, robot):
        super().__init__(robot, utilities.settings.kTop)

    def isFinished(self):
        return super().isFinished()
