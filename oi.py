__author__ = "nikolojedison"

import wpilib
from wpilib.buttons import JoystickButton, InternalButton
from networktables import NetworkTable

from utilities.pov_button import POVButton
from utilities.drive_control import *
from utilities.settings import Settings
import utilities.settings

from macros.play_macro import PlayMacro
from macros.record_macro import RecordMacro

from commands.setpoints.hat_button import HatButton
from commands.setpoints.ears_button import EarsButton
from commands.semiauto.intake import Intake
from commands.setpoints.set_tilt_setpoint import SetTiltSetpoint

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        """Double joysticks WOOT"""

        #Initialise the stick and the smart dashboard (in case we need stuff for auton):
        self.stick = wpilib.Joystick(0)
        self.setpointStick = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Main stick POV.
        #-----------------------------------------------------------------------
        north = POVButton(self.stick, 0)
        northeast = POVButton(self.stick, 45)
        east = POVButton(self.stick, 90)
        southeast = POVButton(self.stick, 135)
        south = POVButton(self.stick, 180)
        southwest = POVButton(self.stick, 225)
        west = POVButton(self.stick, 270)
        northwest = POVButton(self.stick, 315)

        #Main stick buttons.
        #-----------------------------------------------------------------------
        good_trigger = JoystickButton(self.stick, 1)
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
        pov_north = POVButton(self.setpointStick, 0)
        pov_northeast = POVButton(self.setpointStick, 45)
        pov_east = POVButton(self.setpointStick, 90)
        pov_southeast = POVButton(self.setpointStick, 135)
        pov_south = POVButton(self.setpointStick, 180)
        pov_southwest = POVButton(self.setpointStick, 225)
        pov_west = POVButton(self.setpointStick, 270)
        pov_northwest = POVButton(self.setpointStick, 315)


        #Setpoint stick button mapping.
        #-----------------------------------------------------------------------
        bad_trigger = JoystickButton(self.setpointStick, 1)
        thumb = JoystickButton(self.setpointStick, 2)
        bottom_left = JoystickButton(self.setpointStick, 3)
        bottom_right = JoystickButton(self.setpointStick, 4)
        top_left = JoystickButton(self.setpointStick, 5)
        top_right = JoystickButton(self.setpointStick, 6)


        #Goes from front to back. outer_base is the outer ring of buttons on
        #the base, inner_base is the inner ring of buttons on the base.
        #-----------------------------------------------------------------------
        outer_base_one = JoystickButton(self.setpointStick, 7)
        inner_base_one = JoystickButton(self.setpointStick, 8)
        outer_base_two = JoystickButton(self.setpointStick, 9)
        inner_base_two = JoystickButton(self.setpointStick, 10)
        outer_base_three = JoystickButton(self.setpointStick, 11)
        inner_base_three = JoystickButton(self.setpointStick, 12)

        #-----------------------------------------------------------------------

        #Mapping of buttons.
        #-----------------------------------------------------------------------
        thumb_stripe.whileHeld(EarsButton(robot, 1))
        good_trigger.whileHeld(HatButton(robot, 1))
        thumb_normal.whileHeld(Intake(robot, -.5, -.5))

        thumb.whileHeld(EarsButton(robot, 1))
        bad_trigger.whileHeld(HatButton(robot, 1))
        pov_north.whileHeld(Intake(robot, .45, .3))
        pov_south.whileHeld(Intake(robot, -.5, -.5))
        north.whileHeld(Intake(robot, .45, .3))
        south.whileHeld(Intake(robot, -.5, -.5))
        outer_base_one.whileHeld(SetTiltSetpoint(robot, utilities.settings.kTopShot))
        outer_base_two.whileHeld(SetTiltSetpoint(robot, utilities.settings.kShootLevel))
        outer_base_three.whileHeld(SetTiltSetpoint(robot, utilities.settings.kTopShot))
        inner_base_one.whileHeld(SetTiltSetpoint(rbot, utilities.settings.kShootAtBase))
        inner_base_two.whileHeld(SetTiltSetpoint(robot, utilities.settings.kShootRamp))
        inner_base_three.whileHeld(SetTiltSetpoint(robot, utilities.settings.kTopShotAtBase))


    def getStick(self):
        """Drive joystick."""
        return self.stick

    def getSetpointStick(self):
        """Button joystick."""
        return self.setpointStick
