__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointBottom(SetTiltSetpoint):
    """Go to the bottom setpoint"""

    def __init__(self, robot):
        super().__init__(robot, Settings.kBottom)

    def isFinished(self):
        return super().isFinished()
