__author__ = "nikolojedison & auxchar"
#Code copied from 2015_Lopez_Jr. Some changes to fit with 2016 setup.

import wpilib

from utilities.settings import Settings

def precision_mode(controller_input, trigger, button):
    """copied from CubertPy and tweaked for 2016 use."""

    if trigger == True and not button == True:
        #if the trigger is pulled, use the first precision
        return controller_input * Settings.num_precision_one
    elif button == True and not trigger == True:
        #if the thumb button is held, use the second precision
        return controller_input * Settings.num_precision_two
    elif button == True and trigger == True:
        #if both are held, use the combined precision (or a third)
        return controller_input * Settings.num_precision_one * Settings.num_precision_two
    else:
        #if none are held, turn off precision
        return controller_input

def exponential_scaling(base, exponent):

    if base>0:
        return abs(base)**exponent
    else:
        return -(abs(base)**exponent)

def dead_zone(controller_input, dead_zone):
    """Old-style dead zone scaling."""

    if controller_input <= dead_zone and controller_input >= -dead_zone:
        return 0
    elif controller_input > 0:
        return ((controller_input-dead_zone)/(1-dead_zone))
    else:
        return ((-controller_input-dead_zone)/(dead_zone-1))

def drive_control(controller_input, trigger, button):
    """Final thing that's used by the drivetrain class."""
    return precision_mode(exponential_scaling(exponential_scaling(controller_input, 0.5)*0.5, 1.1), trigger, button)
