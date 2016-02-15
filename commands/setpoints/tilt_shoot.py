__author__ = "nikolojedison"

from commands.set_tilt.setpoint import SetTiltSetpoint
import utilities.settings

class TiltShoot(SetTiltSetpoint):
    """Tilt the shooter to the shooting position."""

    def __init__(self, robot):
        super().__init__(robot, settings.kShoot)

    def isFinished(self):
        return super().isFinished()
