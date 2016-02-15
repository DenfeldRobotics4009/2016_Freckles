__author__ = "nikolojedison"

from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class TiltRamp(SetTiltSetpoint):
    """Tilt the shooter to the ramp shooting position."""

    def __init__(self, robot):
        super().__init__(robot, utilities.settings.kRamp)

    def isFinished(self):
        return super().isFinished()
