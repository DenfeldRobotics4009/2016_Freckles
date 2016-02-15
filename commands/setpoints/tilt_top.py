__author__ = "nikolojedison"

from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class TiltTop(SetTiltSetpoint):
    """Tilt the shooter to the top position."""

    def __init__(self, robot):
        super().__init__(robot, utilities.settings.kTop)

    def isFinished(self):
        return super().isFinished()
