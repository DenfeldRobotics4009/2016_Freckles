import math

#Tilt pot setpoints .158
kMaxDown = .800
kMaxUp = kMaxDown - .590
kTop = kMaxUp + .050
kTopShot = .292
kTopShotAtBase = .281
kBottom = kMaxDown - .050
kShootLevel = .646
#Test and modify ^
kShootAtBase = .528
#Test and modify ^
kShootRamp = .400
#Test and modify ^
kLongShot = .645

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.80
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
