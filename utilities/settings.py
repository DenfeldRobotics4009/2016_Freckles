import math

#Tilt pot setpoints
kMaxDown = 0
kMaxUp = 1
kTop = .9
kBottom = .1
kShootLevel = .5
kShootRamp = .7

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.80
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
