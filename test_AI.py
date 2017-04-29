import motor_controller as m
import lazers as l
import time


SPEED = 200
def control_loop():

	while(1):
		front_d = sensor_1.get_distance()
		left_d = sensor_2.get_distance()
		right_d = sensor_3.get_distance()

		if(front_d <= 50):
			print("front_d is zero")
			m.move_stop()
			m.move_left_backward(SPEED)
			m.move_right_backward(SPEED)


		if(left_d == 0):
			print("Turn Right")
			m.move_stop()
			m.move_right_backward(SPEED)
			m.move_left_forward(SPEED)


		if(right_d == 0):
			print("Turn Left")
			m.move_stop()
			m.move_right_forward(SPEED)
			m.move_left_backward(SPEED)
	


[sensor_1, sensor_2, sensor_3] = l.ininitialize()
control_loop()