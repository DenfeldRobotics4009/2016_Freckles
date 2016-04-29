__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointLongShot(SetTiltSetpoint):
    """Move to the long-range shot setpoint."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kLongShot)

    def isFinished(self):
        return super().isFinished()
