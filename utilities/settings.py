import math

#Tilt pot setpoints
kMaxDown = .795
kMaxUp = kMaxDown - .590
kTop = kMaxUp - .030
kBottom = kMaxDown - .030
kShootLevel = kMaxDown - .131
kShootRamp = .400

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.80
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
