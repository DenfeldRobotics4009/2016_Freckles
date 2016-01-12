__author__ = 'nikolojedison'

#May need more libraries in the future, esp. once everything else is properly implemented.
import wpilib
from networktables import NetworkTable
from pov_button import POVButton
from wpilib.buttons import JoystickButton, InternalButton

class OI:
    """Button mapping goes here."""

#If we use the weird drivestation keylistener, remember to port that into its
#own class.

    def __init__(self, robot):
        self.stick = wpilib.Joystick(0)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

    def getStick(self):
        """Drive joystick."""
        return self.stick
