__author__ = "nikolojedison"

from commands.set_tilt.setpoint import SetTiltSetpoint
import utilities.settings

class TiltBottom(SetTiltSetpoint):
    """Tilt the shooter to the bottom position."""

    def __init__(self, robot):
        super().__init__(robot, settings.kBottom)

    def isFinished(self):
        return super().isFinished()
