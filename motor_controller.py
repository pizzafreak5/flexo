import pcduino as pc

speed_left_pin = 10
left_backward_pin = 12
left_forward_pin = 13

speed_right_pin = 9
right_backward_pin = 8
right_forward_pin = 11

pc.pin_mode(speed_left_pin, 'OUTPUT')
pc.pin_mode(left_backward_pin, 'OUTPUT')
pc.pin_mode(left_forward_pin, 'OUTPUT')

pc.pin_mode(speed_right_pin, 'OUTPUT')
pc.pin_mode(right_backward_pin, 'OUTPUT')
pc.pin_mode(right_forward_pin, 'OUTPUT')

def move_stop():
	pc.analog_write(speed_left_pin, 0)
	pc.analog_write(speed_right_pin, 0)

def move_right_forward(speed):
	pc.analog_write(speed_right_pin, speed)
	pc.digital_write(right_forward_pin, pc.HIGH)
	pc.digital_write(right_backward_pin, pc.LOW)

def move_right_backward(speed):
	pc.analog_write(speed_right_pin, speed)
	pc.digital_write(right_forward_pin, pc.LOW)
	pc.digital_write(right_backward_pin, pc.HIGH)

def move_left_forward(speed):
	pc.analog_write(speed_left_pin, speed)
	pc.digital_write(left_forward_pin, pc.HIGH)
	pc.digital_write(left_backward_pin, pc.LOW)


