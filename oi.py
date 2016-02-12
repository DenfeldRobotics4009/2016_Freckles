__author__ = "nikolojedison"

import wpilib
from wpilib.buttons import JoystickButton, InternalButton
from networktables import NetworkTable

from utilities.pov_button import POVButton
from utilities.drive_control import *
from utilities.settings import Settings

from macros.play_macro import PlayMacro
from macros.record_macro import RecordMacro

from commands.setpoints.hat_button import HatButton

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        """This is assuming that the joystick used is the Logitech Extreme 3D."""

        #initialise the stick and the smart dashboard (in case we need stuff for auton):
        self.stick = wpilib.Joystick(0)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Main stick buttons.
        #-----------------------------------------------------------------------
        trigger = JoystickButton(self.stick, 1)
        thumb_stripe = JoystickButton(self.stick, 2)
        trigger_bumper = JoystickButton(self.stick, 3)
        thumb_normal = JoystickButton(self.stick, 4)

        #Throttle buttons.
        #-----------------------------------------------------------------------
        throttle_five = JoystickButton(self.stick, 5)
        throttle_six = JoystickButton(self.stick, 6)
        throttle_seven = JoystickButton(self.stick, 7)
        throttle_eight = JoystickButton(self.stick, 8)
        throttle_nine = JoystickButton(self.stick, 9)
        throttle_ten = JoystickButton(self.stick, 10)

        #Hat switch POV stuff.
        #-----------------------------------------------------------------------
        pov_north = POVButton(self.stick, 0)
        pov_northeast = POVButton(self.stick, 45)
        pov_east = POVButton(self.stick, 90)
        pov_southeast = POVButton(self.stick, 135)
        pov_south = POVButton(self.stick, 180)
        pov_southwest = POVButton(self.stick, 225)
        pov_west = POVButton(self.stick, 270)
        pov_northwest = POVButton(self.stick, 315)

        thumb_stripe.whileHeld(HatButton(robot, -.5))
        trigger.whileHeld(HatButton(robot, .5))

    def getStick(self):
        """Drive joystick."""
        return self.stick
