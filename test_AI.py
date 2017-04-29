import motor_controller as m
import lazers as l
import time

speed_fastest = 255
speed_faster  = 235
speed_fast    = 215
speed_normal  = 195
speed_slow    = 175
speed_slowest = 155




def move_forward(left_d, right_d):
	distance_diff = left_d - right_d
	if abs(distance_diff) <= 10:
		print("Move forward")
		m.move_left_forward(speed_normal)
		m.move_right_forward(speed_normal)
		return

	elif distance_diff <= 40 and distance_diff >=0:
		print("Compensate left")
		m.move_left_forward(speed_normal)
		m.move_right_forward(speed_fast)

	elif distance_diff >= -40 and distance_diff <=0:
		print("Compensate right")
		m.move_left_forward(speed_fast)
		m.move_right_forward(speed_normal)


def move_backward(left_d, right_d):

	distance_diff = left_d - right_d
	if abs(distance_diff) <= 10:

		m.move_left_backward(speed_normal)
		m.move_right_backward(speed_normal)
		return

	elif distance_diff <= 40 and distance_diff >=0:
		# Compensate right backwards
		m.move_right_backward(speed_normal)
		m.move_left_backward(speed_fast)

	elif distance_diff >= -40 and distance_diff <=0:
		# Compensate left backwards 
		m.move_right_backward(speed_fast)
		m.move_left_backward(speed_normal)

def turn_left(left_d, right_d):
	distance_diff = left_d - right_d
	if abs(distance_diff) <= 10:

		m.move_left_forward(speed_slow)
		m.move_right_forward(speed_fast)
		return

def turn_right(left_d, right_d):
	distance_diff = left_d - right_d
	
	if abs(distance_diff) <= 10:
		m.move_left_forward(speed_fast)
		m.move_right_forward(speed_slow)
		return

def control_loop():

	while(1):
		front_d = sensor_1.get_distance()
		left_d = sensor_2.get_distance()
		right_d = sensor_3.get_distance()


		move_forward(left_d,right_d)


		if(front_d <= 100):
			print("Back up")
			move_backward(left_d, right_d)


		if(left_d == 0):
			print("Turn Right")
			turn_right(left_d, right_d)


		if(right_d == 0):
			print("Turn Left")
			turn_left(left_d, right_d)
	
		time.sleep(0.500)	# Sleep for half a second
		m.move_stop()

[sensor_1, sensor_2, sensor_3] = l.ininitialize()
control_loop()