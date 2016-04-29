__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointTopShotAtBase(SetTiltSetpoint):
    """Go to the setpoint for shooting over the back whilst on the ramp."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kTopShotAtBase)

    def isFinished(self):
        return super().isFinished()
