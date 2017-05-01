from pews import *
import motor_controller as mc
import time

front = pew1
right = pew2
left = pew3

default_speeds = {'left':252,'right':255} #left/right. Left could go up a tick or two
adjust_damping = 40
adjust_modifier = 1

adjust_speed = 235

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
    print('L:{}\tF:{}\tR:{}'.format(l_dist_2,f_dist_2,r_dist_2))

    return {'l_dist':l_dist_2,'r_dist':r_dist_2,'f_dist':f_dist_2, 'l_delta':l_delta,'f_delta':f_delta, 'r_delta':r_delta}


def adjust(l_speed, r_speed):

    print('{}:{}',l_speed, r_speed)

    mc.move_right_forward(r_speed)
    mc.move_left_forward(l_speed)
    return

def control_loop():

    mc.move_right_forward(default_speeds['right'])
    mc.move_left_forward(default_speeds['left'])

    time.sleep(0.5)

    dr = right.get_distance()
    dl = left.get_distance()

    #With this,, left WILL override right. But there
    #shouldn't be a situation like this
    if dr < 45:
        adjust(adjust_speed, default_speeds['right'])

    if dl < 45:
        adjust(default_speeds['left'], adjust_speed)

    #run this new speed for half a second

    time.sleep(0.5)
        

    
def start_up():
    time.sleep(5)

start_up()
while (time.clock() < 8):
    control_loop()

mc.move_stop()
