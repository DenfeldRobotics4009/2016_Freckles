import math

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Values that would ideally be changed through drive station
    num_precision_one = 0.60
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
    str_macro_name = "macro.csv"

    #Encoder shenanigans
    kMaxDown = 2850 #(was 2660)
    kMaxUp = 1189 #(was 1121)
