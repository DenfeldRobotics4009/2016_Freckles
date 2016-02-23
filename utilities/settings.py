import math

#Tilt pot setpoints .158
kMaxDown = .790 #derp
#Works so far ^
kMaxUp = kMaxDown - .590
kTop = kMaxUp + .050
kTopShot = .292
kTopShotAtBase = .281
kBottom = kMaxDown - .050
kShootLevel = .646
#Test and modify ^
kShootAtBase = .474
#Test and modify ^
#2nd set of wheels is touching batter
kShootRamp = .326
#Test and modify ^
#Backed into tower
kLongShot = .632
#Works so far ^
#14 feet from tower

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.60
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
