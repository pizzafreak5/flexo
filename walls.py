from pews import *
import motor_controller as mc
import time

front = pew3
right = pew2
left = pew 3

default_speeds = (252,255) #left/right. Left could go up a tick or two


#Note: front delta is probably unessisary, and can be removed to save
#cycles.
def get_delta_diffs():

    l_dist_1 = left.get_distance()
    r_dist_1 = right.get_distance()
    f_dist_1 = front.get_distance()

    time.sleep(0.5)

    l_dist_2 = left.get_distance()
    r_dist_2 = right.get_distance()
    f_dist_2 = front.get_distance()

    l_delta = l_dist_2 - l_dist_1
    r_delta = r_dist_2 - r_dist_1
    f_delta = f_dist_2 - f_dist_1

    return (l_delta, r_delta, f_delta)


def adjust()
