__author__ = "nikolojedison & auxchar"
#Code copied from 2015_Lopez_Jr. Some changes to fit with 2016 setup.

import wpilib

from utilities.settings import Settings

def precision_mode(controller_input, trigger, button):
    """copied from CubertPy, b/c it worked"""

    if trigger:
        return controller_input * Settings.num_precision_one
    elif button:
        return controller_input * Settings.num_precision_two
    else:
        return controller_input

def exponential_scaling(base, exponent):

    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def dead_zone(controller_input, dead_zone):
    """This is the dead zone code, essential for any 4009 'bot."""

    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, trigger, button):
    return precision_mode(exponential_scaling(exponential_scaling(controller_input, 0.5)*0.5, 1.1), trigger, button)
