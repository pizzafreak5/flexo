#re-written to support new startup script, pews.py
# - Garrett

import motor_controller as m
import time
from pews import *

speed_fastest = 255
speed_faster  = 235
speed_fast    = 215
speed_normal  = 195
speed_slow    = 175
speed_slowest = 155




def move_forward(left_d, right_d):
	distance_diff = left_d - right_d
	if abs(distance_diff) <=40:
		print("Move forward")
		m.move_left_forward(speed_faster)
		m.move_right_forward(speed_faster)
		return
<<<<<<< HEAD
	
	elif distance_diff >= 40 and distance_diff >=0:		#Right side is a wall
		print("Compensate left")
		m.move_left_forward(speed_normal)
		m.move_right_forward(speed_fast)

	elif distance_diff <= -40 and distance_diff <=0:		#Left side is wall
		print("Compensate right")
=======

	elif distance_diff <= 40 and distance_diff >=0:
		print("Compensate left") # left is greater than right distance
		m.move_left_forward(speed_normal)
		m.move_right_forward(speed_fast)

	elif distance_diff >= -40 and distance_diff <=0:
		print("Compensate right") # right is greater than left distance
>>>>>>> d4e9f5def34b8c21b9b1a467f7df33614eb2e7a3
		m.move_left_forward(speed_fast)
		m.move_right_forward(speed_normal)



def move_backward(left_d, right_d):
	print("Move backwards")
	m.move_left_backward(speed_fast)
	m.move_right_backward(speed_fast)
	time.sleep(1.500)	# Do this for half a second


def turn_left(left_d, right_d):
<<<<<<< HEAD
	m.move_left_forward(speed_slowest)
	m.move_right_forward(speed_faster)
	time.sleep(1.500)	# Do this for half a second
	return

def turn_right(left_d, right_d):
	m.move_left_forward(speed_faster)
	m.move_right_forward(speed_slowest)
	time.sleep(1.500)	# Do this for half a second
	return

=======
	m.move_left_forward(speed_slow)
	m.move_right_forward(speed_fast)
	return

def turn_right(left_d, right_d):
	
	m.move_left_forward(speed_fast)
	m.move_right_forward(speed_slow)
	return
>>>>>>> d4e9f5def34b8c21b9b1a467f7df33614eb2e7a3

def control_loop():

	count = 1000
	while count > 0:
		front_d = sensor_1.get_distance()
		right_d = sensor_2.get_distance()
		left_d = sensor_3.get_distance()


		move_forward(left_d,right_d)


<<<<<<< HEAD
		if(front_d <= 100):
			move_backward(left_d, right_d)


		if(left_d >= 200):			# Intersection to Left
=======
		if(front_d <= 70):
			print("Back up")
			move_backward(left_d, right_d)


		if(left_d <= 50):
			print("Turn Right")
			turn_right(left_d, right_d)


		if(right_d <= 50): #Unless I'm retarded, this seems like it
                                        #doesn't turn until it crashes into the wall
>>>>>>> d4e9f5def34b8c21b9b1a467f7df33614eb2e7a3
			print("Turn Left")
			turn_left(left_d, right_d)


		if(right_d >= 200):			# Intersection to Right
			print("Turn Right")
			turn_right(left_d, right_d)
	
		time.sleep(0.100)	# Sleep for half a second
		m.move_stop()
		count -= 1


sensor_1 = pew1 #front
sensor_2 = pew2 #right 
sensor_3 = pew3 #left

control_loop()
