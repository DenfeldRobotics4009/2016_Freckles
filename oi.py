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
        """This is assuming that the joystick used is the Logitech Extreme 3D"""
        self.stick = wpilib.Joystick(0)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        trigger = JoystickButton(self.stick, 1)
        thumb = JoystickButton(self.stick, 2)
        bottom_left = JoystickButton(self.stick, 3)
        bottom_right = JoystickButton(self.stick, 4)
        top_left = JoystickButton(self.stick, 5)
        top_right = JoystickButton(self.stick, 6)
        #goes from front to back. outer_base is the outer ring of buttons on
        #the base, inner_base is the inner ring of buttons on the base.
        outer_base_one = JoystickButton(self.stick, 7)
        inner_base_one = JoystickButton(self.stick, 8)
        outer_base_two = JoystickButton(self.stick, 9)
        inner_base_two = JoystickButton(self.stick, 10)
        outer_base_three = JoystickButton(self.stick, 11)
        inner_base_three = JoystickButton(self.stick, 12)

    def getStick(self):
        """Drive joystick."""
        return self.stick
