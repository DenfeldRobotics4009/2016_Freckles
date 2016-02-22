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
from commands.semiauto.shoot import Shoot

from commands.setpoints.tilt_button import TiltButton
from commands.setpoints.tilt.setpoint_bottom import SetpointBottom
from commands.setpoints.tilt.setpoint_long_shot import SetpointLongShot
from commands.setpoints.tilt.setpoint_shoot_base import SetpointShootBase
from commands.setpoints.tilt.setpoint_shoot_level import SetpointShootLevel
from commands.setpoints.tilt.setpoint_shoot_ramp import SetpointShootRamp
from commands.setpoints.tilt.setpoint_top_shot import SetpointTopShot
from commands.setpoints.tilt.setpoint_top_shot_at_base import SetpointTopShotAtBase
from commands.setpoints.tilt.setpoint_top import SetpointTop

class OI:
    """Button mapping goes here."""

    def __init__(self, robot):
        """Double joysticks WOOT"""
        print("Initializing joysticks...")

        #Initialise the stick and the smart dashboard (in case we need stuff for auton):
        self.stick = wpilib.Joystick(0)
        self.setpointStick = wpilib.Joystick(1)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #Main stick POV.
        #-----------------------------------------------------------------------
        drive_north = POVButton(self.stick, 0)
        drive_northeast = POVButton(self.stick, 45)
        drive_east = POVButton(self.stick, 90)
        drive_southeast = POVButton(self.stick, 135)
        drive_south = POVButton(self.stick, 180)
        drive_southwest = POVButton(self.stick, 225)
        drive_west = POVButton(self.stick, 270)
        drive_northwest = POVButton(self.stick, 315)

        #Setpoint stick button mapping.
        #-----------------------------------------------------------------------
        drive_trigger = JoystickButton(self.stick, 1)
        drive_thumb = JoystickButton(self.stick, 2)
        drive_bottom_left = JoystickButton(self.stick, 3)
        drive_bottom_right = JoystickButton(self.stick, 4)
        drive_top_left = JoystickButton(self.stick, 5)
        drive_top_right = JoystickButton(self.stick, 6)


        #Goes from front to back. outer_base is the outer ring of buttons on
        #the base, inner_base is the inner ring of buttons on the base.
        #-----------------------------------------------------------------------
        drive_outer_base_one = JoystickButton(self.setpointStick, 7)
        drive_inner_base_one = JoystickButton(self.setpointStick, 8)
        drive_outer_base_two = JoystickButton(self.setpointStick, 9)
        drive_inner_base_two = JoystickButton(self.setpointStick, 10)
        drive_outer_base_three = JoystickButton(self.setpointStick, 11)
        drive_inner_base_three = JoystickButton(self.setpointStick, 12)


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
        seven = JoystickButton(self.setpointStick, 7)
        eight = JoystickButton(self.setpointStick, 8)
        nine = JoystickButton(self.setpointStick, 9)
        ten = JoystickButton(self.setpointStick, 10)
        eleven = JoystickButton(self.setpointStick, 11)
        twelve = JoystickButton(self.setpointStick, 12)

        #-----------------------------------------------------------------------

        #Mapping of buttons.
        bad_trigger.whileHeld(HatButton(robot, 1))
        thumb.whileHeld(TiltButton(robot))
        pov_north.whileHeld(Intake(robot, .45, .3))
        pov_south.whileHeld(Intake(robot, -.5, -.5))
        bottom_left.whileHeld(EarsButton(robot, 1))
        bottom_right.whileHeld(EarsButton(robot, .4))
        top_left.whileHeld(Intake(robot, -.5, -.5)) #Mini Matt wanted this
        seven.whenPressed(SetpointShootBase(robot))
        eight.whenPressed(SetpointTopShotAtBase(robot))
        nine.whenPressed(SetpointShootLevel(robot))
        ten.whenPressed(SetpointBottom(robot))
        eleven.whenPressed(SetpointLongShot(robot))
        twelve.whenPressed(SetpointTop(robot))

        print("Joysticks initialized")
    def getStick(self):
        """Drive joystick."""
        return self.stick

    def getSetpointStick(self):
        """Button joystick."""
        return self.setpointStick
