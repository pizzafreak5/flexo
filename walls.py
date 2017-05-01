from pews import *
import motor_controller as mc
import time

front = pew3
right = pew2
left = pew3

default_speeds = {'left':252,'right':255} #left/right. Left could go up a tick or two
adjust_damping = 60
adjust_modifier = 1

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


def adjust(l_speed, r_speed):

    mc.move_right_forwards(r_speed)
    mc.move_left_forwards(l_speed)
    return

def control_loop():

    time.sleep(0.25)

    adjust(default_speeds[0], default_speeds[1])

    time.sleep(0.25)

    [delta_left, delta_right, delta_front] = get_delta_diffs()

    if abs(delta_left - delta_right) >=  adjust_damping:
        if delta_left < 0 and delta_right >= 0:
            temp_r_speed = default_speeds[1] - 
    
