from pews import *
import motor_controller as mc
import time

front = pew1
right = pew2
left = pew3

default_speeds = {'left':252,'right':255} #left/right. Left could go up a tick or two
adjust_damping = 40
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

    print('dL:{}\tdF:{}\tdR:{}'.format(l_delta,f_delta,r_delta))

    return {'l_dist':l_dist_2,'r_dist':r_dist_2,'f_dist':f_dist_2, 'l_delta':l_delta,'f_delta':f_delta, 'r_delta':r_delta}


def adjust(l_speed, r_speed):

    mc.move_right_forward(r_speed)
    mc.move_left_forward(l_speed)
    return

def control_loop():

    time.sleep(0.25)

    adjust(default_speeds['left'], default_speeds['right'])

    time.sleep(0.25)

    [dist_right, dist_front, dist_left, delta_left, delta_right, delta_front] = get_delta_diffs()

    if front.get_distance() < 100:
        mc.move_stop()

    elif dist_left <=  adjust_damping:
        if delta_left < 0:
            temp_r_speed = default_speeds['right'] -(adjust_modifier * delta_left)

            time.sleep(0.10)
        elif dist_right <=  adjust_damping:
            temp_l_speed = default_speeds['left'] -(adjust_modifier * delta_right)

            time.sleep(0.10)

def start_up():
    time.sleep(10)

start_up()
while (1):
    control_loop()

mc.move_stop()
