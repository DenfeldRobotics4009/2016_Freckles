__author__ = "nikolojedison"

from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class TiltShoot(SetTiltSetpoint):
    """Tilt the shooter to the shooting position."""

    def __init__(self, robot):
        super().__init__(robot, utilities.settings.kShoot)

    def isFinished(self):
        return super().isFinished()
