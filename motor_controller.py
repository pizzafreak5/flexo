import pcduino as pc

speed_left_pin = 9
left_backward_pin = 11
left_forward_pin = 8

speed_right_pin = 10
right_backward_pin = 13
right_forward_pin = 12


def move_stop():
	pc.analog_write(speed_left_pin, 0)
	pc.analog_write(speed_right_pin, 0)

def move_left_forward(speed):
	pc.analog_write(speed_left_pin, speed)
	pc.digital_write(left_forward_pin, pc.HIGH)
	pc.digital_write(left_backward_pin, pc.LOW)