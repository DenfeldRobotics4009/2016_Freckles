__author__ = "nikolojedison"
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint
from utilities.settings import Settings

class SetpointShootRamp(SetTiltSetpoint):
    """Go to the setpoint for shooting on the ramp, just off the defenses."""

    def __init__(self, robot):
        super().__init__(robot, Settings.kShootRamp)

    def isFinished(self):
        return super().isFinished()
