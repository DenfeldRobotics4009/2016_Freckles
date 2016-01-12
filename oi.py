
__author__ = 'nikolojedison'

#May need more libraries in the future, esp. once everything else is properly implemented.
import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        pass

    def getStick(self):
        """Drive joystick."""
        return self.stick
