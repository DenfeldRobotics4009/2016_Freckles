__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
import utilities.settings

class SetpointShootLevel(SetTiltSetpoint):
    """Fire at the setpoint."""
    kShootLevel = .646
    def __init__(self, robot):
        super().__init__(robot, self.kShootLevel)

    def isFinished(self):
        return super().isFinished()
