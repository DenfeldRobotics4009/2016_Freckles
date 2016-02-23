__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointTopShot(SetTiltSetpoint):
    """Fire at the setpoint."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kTopShot)

    def isFinished(self):
        return super().isFinished()
