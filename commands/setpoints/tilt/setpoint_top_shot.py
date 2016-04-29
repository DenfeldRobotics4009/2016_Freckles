__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointTopShot(SetTiltSetpoint):
    """Go to the setpoint for shooting over the back."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kTopShot)

    def isFinished(self):
        return super().isFinished()
