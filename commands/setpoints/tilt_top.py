__author__ = "nikolojedison"

from commands.set_tilt.setpoint import SetTiltSetpoint
import utilities.settings

class TiltTop(SetTiltSetpoint):
    """Tilt the shooter to the top position."""

    def __init__(self, robot):
        super().__init__(robot, settings.kTop)

    def isFinished(self):
        return super().isFinished()
