__author__ = "nikolojedison"

from commands.set_tilt.setpoint import SetTiltSetpoint
import utilities.settings

class TiltRamp(SetTiltSetpoint):
    """Tilt the shooter to the ramp shooting position."""

    def __init__(self, robot):
        super().__init__(robot, settings.kRamp)

    def isFinished(self):
        return super().isFinished()
