import motor_controller as m
from pews import *
import time
import map_system as ms

front = pew1
right = pew2
left = pew3

#speeds
cali_speed = 190
max_speed = 230
max_vs_cali = max_speed - cali_speed

#times
cali_turn_time = 0.75
motor_rest_time = 1
move_forward_time = 0.1
move_into_intersection_time = 0.6
cross_intersection_time = 1.80
dickered_time = 0.5

#constants
ratio_damp = 0.18
adjust_comp = 0.4
intersection_distance = 253
minimum_distance = 10
dickered_speed = 180

#map_stuff
start = ms.init_map()
current_node = start
next_node = None
start_direction = 'east'
current_direction = start_direction
goal = 'B14'
#states
states = ['traveling', 'start', 'end', 'junction', 'obstacle', 'backup', 'NOPE', 'dickered']
current_state = 'start'

#misc
dickered_flag = 'none'

def turn_90(left):

    global cali_speed, cali_turn_time, motor_rest_time
    
    m.move_stop()
    time.sleep(motor_rest_time)

    if left == True:
        m.move_right_forward(cali_speed)
        m.move_left_backward(cali_speed)
        time.sleep(cali_turn_time)

    else:
        m.move_right_backward(cali_speed)
        m.move_left_forward(cali_speed)
        time.sleep(cali_turn_time)

    m.move_stop()
    time.sleep(motor_rest_time)

def forward(d_left, d_right, f_time = move_forward_time):

    global cali_speed, max_vs_cali, adjust_comp

    d_ratio = float(d_left + 1) / float(d_right + 1)

    

    #faster compensation speed
    comp_speed_f = int(cali_speed + (max_vs_cali * d_ratio * adjust_comp))
    #slower compensation speed
    comp_speed_s = int(cali_speed - (max_vs_cali * d_ratio * adjust_comp))

    if comp_speed_f > 255:
        comp_speed_f = 255

    if d_ratio < 1 - ratio_damp:
        print('Compensate RIGHT: {}<->{}'.format(comp_speed_f, comp_speed_s))
        m.move_left_forward(comp_speed_f)
        m.move_right_forward(comp_speed_s)

    elif d_ratio > 1 + ratio_damp:
        print('Compensate LEFT: {}<->{}'.format(comp_speed_s, comp_speed_f))
        m.move_left_forward(comp_speed_s)
        m.move_right_forward(comp_speed_f)

    else:
        print('FORWARD')
        m.move_left_forward(comp_speed_s)
        m.move_right_forward(comp_speed_f)
    

    time.sleep(f_time)

def control_loop():

    global current_state, next_node, current_node, current_direction, goal, intersection_distance

    print('STATE: {}'.format(current_state))

    if current_state == 'start':

        next_node, direction, end = ms.navigate_single(current_node, goal)

        if end:
            print('The easiest way to win a race is call the start the finish')
            exit()

        if current_direction == direction:
            nop = 0
            #yay
        else:
            nop = 0
            #turn I guess

        current_state = 'traveling'
        forward(100,100)
        

    if current_state == 'traveling':

        d_left = left.get_distance()
        time.sleep(0.02)
        d_right = right.get_distance()
        time.sleep(0.02)
        d_front = front.get_distance()

        if d_left <= minimum_distance and time.clock() > 0.5:
            current_state = 'dickered'
            dickered_flag = 'left'
            m.move_stop()

        elif d_right <= minimum_distance and time.clock() > 0.5:
            current_state = 'dickered'
            dickered_flag = 'right'
            m.move_stop()

        elif d_front <= minimum_distance and time.clock() > 0.5:
            current_state = 'dickered'
            dickered_flag = 'front'
            m.move_stop()

        elif d_left >= intersection_distance or d_right >= intersection_distance:
            current_state = 'junction'
            m.move_stop()
        
        else:
            forward(d_left, d_right)

    if current_state == 'dickered':
        m.move_stop()
        
        time.sleep(motor_rest_time)

        if dickered_flag == 'left':
            m.move_right_backward(dickered_speed + 20)
            m.move_left_backward(dickered_speed)

        if dickered_flag == 'right':
            m.move_right_backward(dickered_speed)
            m.move_left_backward(dickered_speed + 20)

        if dickered_flag == 'front':
            m.move_right_backward(dickered_speed)
            m.move_left_backward(dickered_speed)            

        time.sleep(dickered_time)

        current_state = 'traveling'
        

    if current_state == 'junction':
        m.move_stop()
        time.sleep(motor_rest_time)

        current_node = next_node

        print('REACHED NODE {}'.format(current_node.name))

        next_node, direction, end = ms.navigate_single(current_node, goal)

        if end:
            print('yay, finished')
            exit()

        else:
            dir_to_turn = ms.turn_direction(current_direction, direction)
            front_w, left_w, right_w, back_w = ms.walls(current_direction, current_node)
            print('WALLS: F-{} L-{} R-{} B-{}'.format(front_w, left_w, right_w, back_w))
            
            if dir_to_turn == 'left':
                #move into intersection
                '''
                print('TURNING LEFT')
                forward(100,100, move_into_intersection_time)
                turn_90(True)
                #move into new straight
                forward(100,100, move_into_intersection_time)
                '''
                m.move_left_forward(160)
                m.move_right_forward(200)
                time.sleep(1)
                forward(100,100,0.6)
                current_state = 'traveling'
                        

            if dir_to_turn == 'right':
                #move into intersection
                print('TURNING RIGHT')
                forward(100,100, move_into_intersection_time)
                turn_90(False)
                #move into new straight
                forward(100,100, move_into_intersection_time)
                current_state = 'traveling'

            if dir_to_turn == 'backward': #honestly no idea how this happened
                print('The map says we should go back. No idea')
                current_state = 'NOPE'

            if dir_to_turn == 'forward': #Cross the intersection.
                print('RUNNING THE RED')
                forward(100,100,cross_intersection_time)
                current_state = 'traveling'

            

            current_direction = direction
            m.move_stop()
            
                

    if current_state == 'obstacle':
        nop = 0

    if current_state == 'backup':
        nop = 0

    if current_state == 'NOPE':
        print('REEEEEEEEE')
        m.move_stop()
        exit()

    if current_state == 'end':
        print('Sorry, but the princess is in another castle')
        print('Du du da du da du')
        m.move_stop()
        exit()
    

time.sleep(5)
while (True):
    control_loop()
    
    

