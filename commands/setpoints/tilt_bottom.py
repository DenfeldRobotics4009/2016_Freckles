__author__ = "nikolojedison"

from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class TiltBottom(SetTiltSetpoint):
    """Tilt the shooter to the bottom position."""

    def __init__(self, robot):
        super().__init__(robot, utilities.settings.kBottom)

    def isFinished(self):
        return super().isFinished()
