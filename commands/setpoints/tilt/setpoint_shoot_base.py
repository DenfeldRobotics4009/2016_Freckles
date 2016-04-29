__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointShootBase(SetTiltSetpoint):
    """Go to the setpoint for shooting from the base."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kShootAtBase)

    def isFinished(self):
        return super().isFinished()
