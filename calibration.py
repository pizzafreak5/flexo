import motor_controller as m

import time

def move_forward(speed):
	m.move_right_forward(speed)
	m.move_left_forward(speed)
	
	time.sleep(1)
	m.move_stop()
	time.sleep(1)

def turn_90(stime, speed):
	m.move_right_forward(speed)
	m.move_left_backward(speed)

	time.sleep(stime)
	m.move_stop()
	time.sleep(1)

time.sleep(10)
move_forward(230)
turn_90(0.90,230)


